class InvalidLoginError(Exception):
    """The login provided is invalid."""

    def __init__(
        self,
        argument: str = "Login provided is invalid, please check the email and password",
    ) -> None:
        super().__init__(f"Login error: {argument}")


class InvalidDeviceIDError(Exception):
    """The device ID provided is invalid."""

    def __init__(self) -> None:
        super().__init__("device_id must be a UUID.")


class NotOpenError(Exception):
    """The WebSocket has not been opened."""

    def __init__(self) -> None:
        super().__init__("The WebSocket has not been opened. Call login() first.")


class ResponseError(Exception):
    """General response error."""
