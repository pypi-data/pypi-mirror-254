"""Serial connection to arduino to interact with Kengo's setup."""
import logging
import time

import serial

from trigger_count.log import get_basic_logger


BAUDRATE = 9600
PORT = "/dev/ttyACM0"
TRIAL_START_COMMAND = "d"
STIM_START_COMMAND = "B"
TRIAL_END_COMMAND = "T"


class TriggerOutArduino:
    """Class that implements serial connection to arduino."""
    def __init__(
            self,
            port: str = PORT,
            baudrate: int = BAUDRATE,
            logger: logging.Logger | None = None,
    ) -> None:
        self._port = port
        self._baudrate = baudrate
        self.logger = logger
        if self.logger is None:
            self.logger = get_basic_logger("kengo_arduino")

        # go
        self._serial = serial.Serial(
            baudrate=baudrate,
            port=port,
        )
        self.logger.info(f"Port {self._port}: Serial connection established.")
        time.sleep(1)

    def send_trial_trigger(self) -> None:
        """Send trigger for trial start."""
        self._serial.write(TRIAL_START_COMMAND.encode())
        self.logger.info(f"Trial trigger -> Command: {TRIAL_START_COMMAND}")

    def send_stim_trigger(self) -> None:
        self._serial.write(STIM_START_COMMAND.encode())
        self.logger.info(f"Stim trigger -> Command: {STIM_START_COMMAND}")

    def send_stop_trigger(self) -> None:
        self._serial.write(TRIAL_END_COMMAND.encode())
        self.logger.info(f"Stop trigger -> Command: {STIM_START_COMMAND}")

    def close(self) -> None:
        self._serial.close()
        self.logger.info(f"Port {self._port}: Serial connection closed.")
