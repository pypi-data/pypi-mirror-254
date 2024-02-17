from enum import Enum

SERVICE_URL = "wss://linr-cs-tm-prod.trafficmanager.net:8080/Message.svc"  # One URL for everything


class MessageTypes(Enum):
    HELLO = "HELLO"
    KEEPALIVE = "keepalive"
    REQUEST_SITE_LIST = "REQUEST_SITE_LIST"
    REQUEST_DEVICE_STATE = "REQUEST_DEVICE_STATE"
    REQUEST_HISTORY = "REQUEST_HISTORY"
    SITE_LIST = "SITE_LIST"
    GOODBYE = "GOODBYE"
    REQUEST_SITE_CONFIG = "REQUEST_SITE_CONFIG"
    SITE_CONFIG = "SITE_CONFIG"
    OPERATE_DEVICE = "OPERATE_DEVICE"
    DEVICE_STATE = "DEVICE_STATE"
    WELCOME = "WELCOME"


TYPE_TO_PROTOCOL = {
    MessageTypes.HELLO: "CMP/1.0",
    MessageTypes.KEEPALIVE: "ECHO/1.0",
    MessageTypes.REQUEST_SITE_LIST: "SMP/1.0",
    MessageTypes.REQUEST_DEVICE_STATE: "ACP/1.0",
    MessageTypes.REQUEST_HISTORY: "ERP/1.0",
    MessageTypes.REQUEST_SITE_CONFIG: "SMP/1.0",
    MessageTypes.OPERATE_DEVICE: "ACP/1.0",
    MessageTypes.DEVICE_STATE: "ACP/1.0",
}
