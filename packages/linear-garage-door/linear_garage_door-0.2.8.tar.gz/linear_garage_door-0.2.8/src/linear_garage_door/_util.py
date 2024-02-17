from __future__ import annotations

from typing import Any

from .const import TYPE_TO_PROTOCOL, MessageTypes


def parse_response(resp: str) -> dict[str, Any]:
    response_dict: dict[str, Any] = {
        "Type": "",
        "Headers": {},
        "Body": "",
    }
    response = resp.split("\r\n")

    for i in range(1, len(response)):
        line = response[i]
        if line == "":
            break
        response_dict["Headers"][line.split(":")[0]] = ":".join(line.split(":")[1:])

    response_dict["Type"] = response[0].split(" ")[1]

    return response_dict


def create_request(msg_type: MessageTypes, data: dict[str, str]) -> str:
    request_string = f"{TYPE_TO_PROTOCOL[msg_type]} {msg_type.value}\r\n"

    for key in data.keys():
        request_string += f"{key}:{data[key]}\r\n"

    request_string += "\r\n"

    return request_string
