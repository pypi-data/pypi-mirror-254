"""
Module for interation with arduino that sends TTL pulses to stimulus computer.

For this to work, an arduino needs to:
- Wait to receive a 'p' through serial connection
- Start sending TTL pulses after 'p'
- Check for stop messages while sending TTL pulses
- Stop when receiving an 'x'
"""
import datetime
import time
from pathlib import Path

import pandas as pd
import serial


class TtlArduino:
    """Serial connection to an arduino that sends TTL pulses."""

    def __init__(self, port_name: str, baud_rate: int, csv_file: Path) -> None:
        self.csv_file: Path = csv_file
        self.serial_connection: serial.Serial = serial.Serial(
            port=port_name,
            baudrate=baud_rate,
        )
        print(f"Serial connection to arduino on port {port_name} established.")

        self.i_ttl: int = 0

    def run(self) -> None:
        """Main method to call."""
        self.send_start_signal()
        self.run_ttl_loop()
        self.send_stop_signal()
        self.check_for_messages_after_stop()

    def run_ttl_loop(self) -> None:
        """In a loop, catch and record messages from arduino."""
        while True:
            try:
                self.record_ttl_message()
            except KeyboardInterrupt:
                break

    def record_ttl_message(self) -> None:
        """Receive a TTL message from the arduino, then save it with a timestamp to a csv file."""
        message: bytes = self.serial_connection.readline()
        message: str = message.decode().strip()
        timestamp = datetime.datetime.now()
        self.save_ttl_timestamp(timestamp, message)

    def save_ttl_timestamp(self, timestamp: datetime.datetime, message: str) -> None:
        """Save TTL message timestamp to a csv file."""
        microseconds, ttl_count = message.split("\t")
        ttl_info = {
            "timestamp": timestamp,
            "i_ttl": self.i_ttl,
            "arduino_ttl_count": ttl_count,
            "arduino_runtime_microseconds": microseconds,
        }
        ttl_info = pd.DataFrame([ttl_info])
        if self.i_ttl == 0:
            ttl_info.to_csv(self.csv_file, mode="w", header=True)
        else:
            ttl_info.to_csv(self.csv_file, mode="a", header=False)

        if self.i_ttl % 100 == 0:
            print(f"{timestamp}: {ttl_count=}, {microseconds=}")

        self.i_ttl += 1

    def send_start_signal(self) -> None:
        """Ask arduino to start sending TTL pulses."""
        input("Press enter to start pulse sending: ")
        print(f"{datetime.datetime.now()}: Arduino should be sending TTL pulses from now on.")

        message = "p".encode()
        self.serial_connection.write(message)

    def send_stop_signal(self) -> None:
        """Ask arduino to stop sending TTL pulses."""
        message = "x".encode()
        print(f"{datetime.datetime.now()}: Arduino should not be sending TTL pulses from now on.")
        self.serial_connection.write(message)

    def check_for_messages_after_stop(self) -> None:
        """Check whether arduino still sends TTl messages after stop signal."""
        print("Checking for TTL messages after stop signal.")
        last_time = time.time()
        i_message = 0
        while (time.time() - last_time) < 5:
            if self.serial_connection.in_waiting:
                self.record_ttl_message()
                last_time = time.time()
                i_message += 1
        print(f"Received {i_message} message(s) after sending stop signal.")
