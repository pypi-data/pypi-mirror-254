"""Control Linear Garage Doors."""

from __future__ import annotations

import asyncio
import logging
import uuid
from typing import Any, Awaitable, Callable

import aiohttp

from ._util import create_request
from .const import MessageTypes
from .errors import InvalidDeviceIDError, InvalidLoginError, NotOpenError, ResponseError
from .ws import WebSocketMonitor


class Linear:
    """A Linear account.

    Instantiate this class then run [`login()`][linear_garage_door.Linear.login] with your credentials to connect.

    Example:
        ```python
        from linear_garage_door import Linear

        async def on_device_state_event(data: dict[str, dict[str, str] | str]):
            print(data)

        linear = Linear(on_device_state_event=on_device_state_event)

        # Log in to the account
        await linear.login("email@email.com", "password", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

        # Get the sites on the account
        sites = await linear.get_sites()

        # Loop through each site and get the devices
        for site in sites:
            devices = await linear.get_devices(site["id"])
            for device in devices:
                print("")
                print(device["name"], "----")
                device_state = await linear.get_device_state(device["id"])
                for key in device_state.keys():
                    print(key, "--")
                    print("")
                    for attribute in device_state[key].keys():
                        print(attribute, "=", device_state[key][attribute])
                    print("")

        await linear.close()
        ```
    """

    _message_id = -1
    _ws: aiohttp.ClientWebSocketResponse
    _device_id: str
    _logger: logging.Logger
    _debug: bool = False
    _user_id: str
    _user_email: str
    _internal_callback: Callable[[dict[str, Any]], Awaitable[None]] | None = None
    _monitor: WebSocketMonitor
    _keepalive_task: asyncio.Task[None]

    def __init__(
        self: Linear,
        on_device_state_event: Callable[[dict[str, Any]], Awaitable[None]]
        | None = None,
    ):
        """Initialize the Linear account.

        Args:
            on_device_state_event (function | None, optional): Pass a function to subscribe to device state events. The function provided will be called with the data similar to the data returned by [`login()`][linear_garage_door.Linear.login]. Defaults to None.
        """
        self._logger = logging.getLogger("linear_garage_door")
        self._debug = self._logger.isEnabledFor(logging.DEBUG)
        self.on_device_state_event = on_device_state_event

    @property
    def open(self: Linear) -> bool:
        return not self._ws.closed

    def _get_message_id(self: Linear) -> str:
        self._message_id += 1
        message_id = hex(self._message_id)[2:].zfill(8).upper()

        return message_id

    def _verify_device_id(self: Linear, device_id: str | None) -> str:
        if device_id is None:
            device_id = str(uuid.uuid4()).upper()
            self._logger.warning(
                "No device_id provided. Proceeding with random UUID. Please use this UUID in future calls to this function: %s",
                device_id,
            )
        else:
            valid = True
            try:
                uuid.UUID(str(device_id))
            except ValueError:
                valid = False

            if not valid:
                raise InvalidDeviceIDError()
            else:
                device_id = device_id.upper()

        return device_id

    async def _await_for_any_msg(self: Linear) -> dict[str, Any]:
        future: asyncio.Future[dict[str, Any]] = asyncio.Future()

        async def _got_resp(data: dict[str, Any]) -> None:
            future.set_result(data)
            self._internal_callback = None

        self._internal_callback = _got_resp

        result = await asyncio.wait_for(future, timeout=10.0)

        return result

    async def _await_for_msg_type(
        self: Linear, msg_type: str, timeout: float = 10.0
    ) -> dict[str, Any]:
        future: asyncio.Future[dict[str, Any]] = asyncio.Future()

        async def _got_resp(data: dict[str, Any]) -> None:
            if data["Type"] == msg_type:
                future.set_result(data)
                self._internal_callback = None

        self._internal_callback = _got_resp

        result = await asyncio.wait_for(future, timeout=timeout)

        return result

    async def _await_for_dev_state_report(
        self: Linear, device_id: str
    ) -> dict[str, Any]:
        future: asyncio.Future[dict[str, Any]] = asyncio.Future()

        async def _got_resp(response: dict[str, Any]) -> None:
            if (
                response["Type"] == MessageTypes.DEVICE_STATE.value
                and response["Headers"]["Type"] == "Report"
                and response["Headers"]["SendingDeviceID"] == "H/" + device_id
            ):
                future.set_result(response)
                self._internal_callback = None

        self._internal_callback = _got_resp

        result = await asyncio.wait_for(future, timeout=10.0)

        return result

    async def _message_callback(self: Linear, data: dict[str, Any]) -> None:
        if self._internal_callback:
            # Override user-provided callback
            await self._internal_callback(data)
        elif self.on_device_state_event:
            await self.on_device_state_event(data)

    def _check_if_open(self: Linear) -> None:
        if not self.open:
            raise NotOpenError()

    async def _keepalive(self: Linear) -> None:
        while True:
            if not self.open:
                return

            request = create_request(
                MessageTypes.KEEPALIVE,
                {
                    "MessageID": self._get_message_id(),
                    "SendingUserID": self._user_id,
                    "Targets": "B/*",
                    "SendingDeviceID": self._device_id,
                },
            )
            await self._ws.send_str(request)
            try:
                await self._await_for_msg_type(MessageTypes.KEEPALIVE.value)
            except asyncio.TimeoutError as e:
                raise ResponseError from e

            await asyncio.sleep(540)

    async def login(
        self: Linear,
        email: str,
        password: str,
        device_id: str | None = None,
        client_session: aiohttp.ClientSession | None = None,
    ) -> dict[str, Any] | None:
        """Logs in to a Linear account.

        Tip:
            Need a device ID? Grab one [here](https://www.uuidgenerator.net/version4).

        Example:
            ```python
            from linear_garage_door import Linear

            linear = Linear()
            await linear.login("email@email.com", "password", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

            await linear.close()
            ```

        Args:
            email (str): The email of the account to log in to.
            password (str): The password of the account to log in to.
            device_id (str | None, optional): The device ID of your choice. Must be a UUID. Defaults to a random UUID.

        Raises:
            InvalidLogin: The login provided is invalid.
            InvalidDeviceID: The device ID provided is invalid.

        Returns:
            A dict with the type of response, most likely "WELCOME", the headers of the response, and the body.
        """

        try:
            if self.open:
                return None
        except AttributeError:
            pass

        self._device_id = "M/" + self._verify_device_id(device_id)
        request = create_request(
            MessageTypes.HELLO,
            {
                "MessageID": self._get_message_id(),
                "UserEmail": email,
                "Password": password,
                "TargetsHere": self._device_id,
                "Targets": "B/*",
                "SendingDeviceID": self._device_id,
            },
        )

        ws_monitor = WebSocketMonitor()
        if ws_monitor.websocket is None or ws_monitor.websocket.closed:
            if client_session is None:
                await ws_monitor.new_connection(
                    aiohttp.ClientSession(), self._message_callback, True, False
                )
            else:
                await ws_monitor.new_connection(
                    client_session, self._message_callback, True, True
                )
        if ws_monitor.monitor is None or ws_monitor.monitor.done():
            await ws_monitor.start_monitor()
        ws = ws_monitor.websocket

        # Start keepalive task
        self._keepalive_task = asyncio.create_task(self._keepalive())

        assert ws is not None

        self._monitor = ws_monitor
        self._ws = ws

        response = asyncio.create_task(self._await_for_any_msg())

        await ws.send_str(request)

        response_data = await response

        if (
            response_data["Type"] == MessageTypes.GOODBYE.value
            and response_data["Headers"]["UserID"] == ""
        ):
            if response_data["Headers"]["Reason"] == "InvalidLogin":
                raise InvalidLoginError()

            raise InvalidLoginError(response_data["Headers"]["Reason"])

        self._user_id = response_data["Headers"]["UserID"]
        self._user_email = response_data["Headers"]["UserEmail"]

        return response_data

    async def get_sites(self: Linear) -> list[dict[str, str]]:
        """Get sites available under this account.

        Example:
            ```python
            from linear_garage_door import Linear

            linear = Linear()
            await linear.login("email@email.com", "password", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

            sites = await linear.get_sites()
            for site in sites:
                print(site["name"], "has id", site["id"])

            await linear.close()
            ```

        Raises:
            NotOpen: The WebSocket has not been opened.

        Returns:
            A list of dicts that contain the device's ID and name.
        """

        self._check_if_open()

        request = create_request(
            MessageTypes.REQUEST_SITE_LIST,
            {
                "MessageID": self._get_message_id(),
                "SendingUserID": self._user_id,
                "Targets": "B/*",
                "SendingDeviceID": self._device_id,
            },
        )

        response = asyncio.create_task(
            self._await_for_msg_type(MessageTypes.SITE_LIST.value)
        )
        await self._ws.send_str(request)
        response_data = await response

        sites = []

        for key in response_data["Headers"].keys():
            if key.startswith("Site-"):
                site = response_data["Headers"][key].split(",")
                sites.append({"id": site[0], "name": site[1]})

        return sites

    async def get_devices(self: Linear, site: str) -> list[dict[str, list[str] | str]]:
        """Get devices available under a specific site.

        Example:
            ```python
            from linear_garage_door import Linear

            linear = Linear()
            await linear.login("email@email.com", "password", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

            sites = await linear.get_sites()
            for site in sites:
                devices = await linear.get_devices(site["id"])
                for device in devices:
                    print(device["name"], "(", device["id"], ") has the following subdevices:")
                    for subdevice in device["subdevices"]:
                        print(subdevice)

            await linear.close()
            ```

        Args:
            site (str): The site ID to fetch the devices from. Get site IDs by calling [`get_sites()`][linear_garage_door.Linear.get_sites].

        Raises:
            NotOpen: The WebSocket has not been opened.

        Returns:
            A list of dictionaries that contains the ID, name, and subdevices of that device. (Subdevices usually are GDO, Light, etc...)
        """

        self._check_if_open()

        request = create_request(
            MessageTypes.REQUEST_SITE_CONFIG,
            {
                "MessageID": self._get_message_id(),
                "SendingUserID": self._user_id,
                "Targets": "B/*",
                "SiteID": site,
                "SendingDeviceID": self._device_id,
            },
        )

        response = asyncio.create_task(
            self._await_for_msg_type(MessageTypes.SITE_CONFIG.value)
        )
        await self._ws.send_str(request)
        response_data = await response

        devices = []

        for key in response_data["Headers"].keys():
            if key.startswith("HDev-"):
                device = response_data["Headers"][key].split(",")
                devices.append(
                    {
                        "id": device[0],
                        "name": device[1],
                        "subdevices": [i.replace("\\", "") for i in device[5:]],
                    }
                )

        return devices

    async def operate_device(
        self: Linear, device_id: str, subdevice: str, subdevice_state: str
    ) -> None:
        """Operate a device.

        Here are the known states for each subdevice:

        - `GDO`: `Open` or `Close` (Not `Closed`!)
        - `Light`: `On` or `Off`

        More reverse engineering will be required in the future for setting the Light brightness and getting the progress of door opening.

        This does not return anything. Events will be fired from the server and can give you a state.

        Example:
            ```python
            from linear_garage_door import Linear

            linear = Linear()

            await linear.login("email@email.com", "password", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

            await linear.operate_device(device["id"], "GDO", "Open")
            ```

        Args:
            device_id (str): The device ID you want to operate. You can get this from [`get_devices()`][linear_garage_door.Linear.get_devices]
            subdevice (str): The subdevice you want to operate. The list of subdevices is also available from [`get_devices()`][linear_garage_door.Linear.get_devices]
            subdevice_state (str): The state to set the subdevice to. I don't know where the full list of states are, but you can get a good guess from [`get_device_state()`][linear_garage_door.Linear.get_device_state]

        Raises:
            NotOpen: The WebSocket has not been opened.
        """

        self._check_if_open()

        # Send HELLO request to device

        hello_request = create_request(
            MessageTypes.HELLO,
            {
                "MessageID": self._get_message_id(),
                "SendingUserID": self._user_id.upper(),
                "UserEmail": self._user_email,
                "TargetsHere": self._device_id,
                "Targets": device_id,
                "SendingDeviceID": self._device_id,
            },
        )

        await self._ws.send_str(hello_request)

        op_request = create_request(
            MessageTypes.OPERATE_DEVICE,
            {
                "MessageID": self._get_message_id(),
                "SendingUserID": self._user_id.upper(),
                "SubDev-" + subdevice: subdevice_state,
                "Targets": "H/" + device_id,
                "SendingDeviceID": self._device_id,
            },
        )

        await self._ws.send_str(op_request)

        await self._await_for_msg_type(MessageTypes.DEVICE_STATE.value)

        return

    async def get_device_state(
        self: Linear, device_id: str
    ) -> dict[str, dict[str, str]]:
        """Get state of device.

        Example:
            ```python
            from linear_garage_door import Linear

            async def on_device_state_event(data: dict[str, dict[str, str] | str]):
                print(data)

            linear = Linear(on_device_state_event=on_device_state_event)

            # Log in to the account
            await linear.login("email@email.com", "password", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

            # Get the sites on the account
            sites = await linear.get_sites()

            # Loop through each site and get the devices
            for site in sites:
                devices = await linear.get_devices(site["id"])
                for device in devices:
                    print("")
                    print(device["name"], "----")
                    device_state = await linear.get_device_state(device["id"])
                    for key in device_state.keys():
                        print(key, "--")
                        print("")
                        for attribute in device_state[key].keys():
                            print(attribute, "=", device_state[key][attribute])
                        print("")

            await linear.close()
            ```

        Args:
            device_id (str): The device ID to get the state of.

        Raises:
            NotOpen: The WebSocket has not been opened.

        Returns:
            A dictionary that shows each subdevice and their respective states.
        """

        self._check_if_open()

        # Send HELLO request to device

        hello_request = create_request(
            MessageTypes.HELLO,
            {
                "MessageID": self._get_message_id(),
                "SendingUserID": self._user_id.upper(),
                "UserEmail": self._user_email,
                "TargetsHere": self._device_id,
                "Targets": device_id,
                "SendingDeviceID": self._device_id,
            },
        )

        awaiting_welcome = asyncio.create_task(
            self._await_for_msg_type(MessageTypes.WELCOME.value, timeout=2.0)
        )

        await self._ws.send_str(hello_request)

        try:
            await awaiting_welcome
        except asyncio.TimeoutError:
            pass

        state_request = create_request(
            MessageTypes.REQUEST_DEVICE_STATE,
            {
                "MessageID": self._get_message_id(),
                "SendingUserID": self._user_id.upper(),
                "Targets": "H/" + device_id,
                "SendingDeviceID": self._device_id,
            },
        )

        response = asyncio.create_task(self._await_for_dev_state_report(device_id))

        await self._ws.send_str(state_request)

        response_data = await response

        subdev_props: dict[str, dict[str, str]] = {}

        for key in response_data["Headers"].keys():
            if key.startswith("SubDev-"):
                subdev_name = key.split("SubDev-")[1]
                subdev_props[subdev_name] = {}

                subdev = response_data["Headers"][key].split(",")

                for prop in subdev:
                    subdev_props[subdev_name][prop.split(":")[0]] = prop.split(":")[1]

        return subdev_props

    async def close(self: Linear) -> None:
        """Close the WebSocket."""
        self._keepalive_task.cancel()
        await self._monitor.close()
