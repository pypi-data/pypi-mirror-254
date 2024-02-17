from PyQt6.QtDBus import QDBusMessage
from typing import TYPE_CHECKING
from .DBusType import DBusType
from lxml import etree


if TYPE_CHECKING:
    from .Interface import Interface


class Signal:
    def __init__(self) -> None:
        self.name = ""
        self.is_connected = False
        self.interface: "Interface" | None = None

    @classmethod
    def from_xml(obj, interface: "Interface", element: etree._Element):
        signal = obj()
        signal.interface = interface

        signal.name = element.get("name")

        return signal
