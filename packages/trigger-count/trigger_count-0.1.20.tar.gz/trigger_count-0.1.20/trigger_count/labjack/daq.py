"""
Fast labjack - should be able to read 4 counters with roughly 1000 Hz
This should make it easier to detect faulty triggers.

Run this in subprocess while running stimuli in main process.
"""

import datetime
import logging
import time
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from trigger_count.labjack.counter import CounterLabjack


TIMEOUT_DURATION = 10


class FastLabjackDaq(CounterLabjack):
    """Daq with fast sampling."""

    def __init__(self, output_folder: Path) -> None:
        super().__init__()
        # params
        self.output_folder: Path = output_folder

        # files
        self.daq_file: Path = self.output_folder / "labjack.csv"
        self.instant_file: Path = self.output_folder / "instant.txt"

        # state
        self.count: int = 0
        self.last_reads: dict | None = None
        self.last_time: datetime.datetime | None = None
        self.time_since_increase: dict | None = None
        self.intervals: dict | None = None
        self.keep_waiting: bool = False
        self.increases_per_counter: dict | None = None
        self.is_ready_per_counter: dict | None = None
        self.n_increases: int = 5
        self.keep_running: bool = True
        self.last_change: datetime.datetime | None = None
        self.logger = self.create_logger()

    def create_logger(self) -> logging.Logger:
        logger = logging.getLogger("labjack")
        logger.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler(stream=sys.stdout)
        stream_formatter = logging.Formatter("%(name)s - %(message)s")
        stream_handler.setFormatter(stream_formatter)
        stream_handler.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(self.output_folder / "labjack.log")
        file_formatter = logging.Formatter("%(asctime)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.DEBUG)

        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        return logger

    def start_recording(self) -> None:
        """Start recording."""
        self.assert_no_running_counters()
        self.wait_for_counters_to_increase()

    def assert_no_running_counters(self) -> None:
        """Confirm that no counters have started."""
        for i in range(5):
            reads = self.read_all_counters()
            for counter, value in reads.items():
                if value != 0:
                    raise ValueError(f"Counter {counter} is running -> {value} != 0")
            time.sleep(0.5)
        self.logger.info("No running counters.")

    def wait_for_counters_to_increase(self) -> None:
        """Block until all counters have increased."""
        self.keep_waiting = True
        counter_names = list(self.counters.keys())
        self.increases_per_counter = {name: 0 for name in counter_names}
        self.is_ready_per_counter = {name: False for name in counter_names}
        self.logger.info(f"Waiting on counters to increase: {counter_names}")
        while self.keep_waiting:
            row, current_time, current_reads = self.sample()
            if self.count > 0:
                self.check_increase(current_reads)
            self.write(row, current_reads)
            self.update(current_time, current_reads)
        self.logger.info("All counters have increased.")

    def check_increase(self, current_reads: dict) -> None:
        """Check whether current reads differ from last reads."""
        all_counters = np.asarray(list(self.is_ready_per_counter.keys()))
        for name, new_value in current_reads.items():
            if new_value != self.last_reads[name]:
                self.increases_per_counter[name] += 1
                if not self.is_ready_per_counter[name]:
                    self.logger.info(f"Counter {name} is increasing -> {new_value}")
                    if self.increases_per_counter[name] > self.n_increases:
                        self.is_ready_per_counter[name] = True
                        self.logger.info(f"Counter {name} is ready.")
                        is_ready = np.asarray(list(self.is_ready_per_counter.values()))
                        if np.all(is_ready):
                            self.keep_waiting = False
                        else:
                            is_missing = np.logical_not(is_ready)
                            missing_counters = all_counters[is_missing]
                            self.logger.info(f"Still waiting on {missing_counters}")

    def run(self) -> None:
        """Main method to call. Samples labjack with 1000 Hz."""
        assert isinstance(self.main_counter, str)
        self.logger.info(f"Scanning all counters from now on.")
        while self.keep_running:
            row, current_time, current_reads = self.sample()
            self.write(row, current_reads)
            self.update(current_time, current_reads)
            self.check_timeout(current_time)
        self.logger.info(f"All counters did not increase for {TIMEOUT_DURATION}s.")
        self.logger.info("Scan completed.")

    def sample(self) -> tuple:
        """Read all counters, add timestamp."""
        current_time = datetime.datetime.now()
        current_reads = self.read_all_counters()
        if self.count == 0:
            row_elapsed = None
            self.time_since_increase = {f"time_{name}": 0 for name in current_reads.keys()}
            self.intervals = {f"interval_{name}": None for name in current_reads.keys()}
        else:
            row_elapsed = (current_time - self.last_time).total_seconds()
            for name, val in current_reads.items():
                if self.last_reads[name] != val:
                    interval = self.time_since_increase[f"time_{name}"] + row_elapsed
                    self.intervals[f"interval_{name}"] = interval
                    self.time_since_increase[f"time_{name}"] = 0
                    self.last_change = current_time
                else:
                    self.intervals[f"interval_{name}"] = None
                    self.time_since_increase[f"time_{name}"] += row_elapsed
        row = {
            "count": self.count,
            "datetime": current_time,
            "elapsed": row_elapsed,
        }
        row.update(current_reads)
        row.update(self.time_since_increase)
        row.update(self.intervals)
        return row, current_time, current_reads

    def write(self, row: dict, current_reads: dict) -> None:
        """Write info to files."""
        if self.count == 0:
            pd.DataFrame([row]).to_csv(self.daq_file, mode="w", header=True)
        else:
            pd.DataFrame([row]).to_csv(self.daq_file, mode="a", header=False)
        with open(self.instant_file, mode="w") as file:
            file.write(str(current_reads[self.main_counter]))

    def update(self, current_time: datetime.datetime, current_reads: dict) -> None:
        """Update state."""
        self.count += 1
        self.last_time = current_time
        self.last_reads = current_reads

    def check_timeout(self, current_time: datetime.datetime) -> None:
        """Check whether any counter has increased in a while"""
        if self.last_change is not None:
            elapsed = (current_time - self.last_change).total_seconds()
            if elapsed > TIMEOUT_DURATION:
                self.keep_running = False


if __name__ == "__main__":
    daq = FastLabjackDaq(Path("/home/pennartz/Mathis/gitlab/trigger_count/results"))
    daq.add_counter("widefield_camera", "DIO0")
    # labjack.add_counter("vitals_monitor", "DIO1")
    # labjack.add_counter("left_eye_camera", "DIO2")
    # labjack.add_counter("right_eye_camera", "DIO3")
    daq.set_main_counter("widefield_camera")
    daq.start_recording()
    daq.run()

