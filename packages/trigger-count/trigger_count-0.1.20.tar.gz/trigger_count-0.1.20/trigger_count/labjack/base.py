"""
Module for basic labjack interactions.
Tested only with Labjack T7 Pro.
"""
import time

from labjack import ljm


class BaseLabjack:
    """Basic class to use labjack as a data acquisition system (labjack)."""

    def __init__(self) -> None:
        """Open connection to labjack."""
        self.handle = ljm.openS("T7", "ANY", "ANY")

    def read_single_port(self, port_name: str) -> float:
        """Read value from labjack port."""
        value = ljm.eReadName(self.handle, port_name)
        return value

    def read_multiple_ports(self, port_names: list) -> list:
        values = ljm.eReadNames(self.handle, len(port_names), port_names)
        return values

    def send_ttl(self, port_name: str = "DAC0", duration_ms: float = 1) -> None:
        """Send a simple TTL pulse."""
        ljm.eWriteName(self.handle, port_name, 10)
        time.sleep(duration_ms / 1000)
        ljm.eWriteName(self.handle, port_name, 0)

