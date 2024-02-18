"""
Subsample labjack.csv file from ~1000 Hz to frame rate.
Then add stim info to get a table with one row per imaging frame.
"""
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from tqdm import tqdm


class Daq2FrameConverter:
    """Implements combination of labjack and stim info to frame info."""
    def __init__(
            self,
            source_folder: Path,
            n_tif_frames: int,
            frame_trigger_in_daq: str,
            start_offset: int = 0,
            end_offset: int = 0,
            frame_trigger_in_stim: str = "counter",
            stim_columns_to_rename: dict | None = None,
            other_daq_triggers: list | None = None,
            vitals_file: Path | None = None
    ) -> None:
        # params
        self.source_folder = source_folder
        self.n_tif_frames: int = n_tif_frames
        self.frame_trigger_in_daq = frame_trigger_in_daq
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.frame_trigger_in_stim = frame_trigger_in_stim
        self.stim_columns_to_rename = stim_columns_to_rename
        self.other_daq_triggers = other_daq_triggers
        self.vitals_file = vitals_file
        self.vitals_available = isinstance(vitals_file, Path)

        # other
        self.daq_file = self.source_folder / "daq.csv"
        self.stim_file = self.source_folder / "flip_info.csv"
        self.recording_type = None
        self.daq_table = None
        self.stim_table = None
        self.vitals_table = None

        self.frame_table = None

        self.check_paths()

    def check_paths(self) -> None:
        """Check whether all files exist."""
        assert self.daq_file.is_file(), f"{self.daq_file} not a file"
        assert self.stim_file.is_file()

    def run(self) -> pd.DataFrame:
        """Main method to call."""
        self.determine_recording_type()
        self.read_files()
        self.print_samples()
        if isinstance(self.stim_columns_to_rename, dict):
            self.rename_stim_columns()
        self.subtract_extra_start()
        self.subsample_daq()
        self.check_triggers()
        self.check_intervals()
        self.combine_daq_and_stim()
        self.clean_up()
        self.compare()
        return self.frame_table

    def determine_recording_type(self) -> None:
        self.recording_type = "widefield" if "widefield" in self.frame_trigger_in_daq else "twophoton"
        print(f"Recording type: {self.recording_type}")

    def read_files(self) -> None:
        """Read csv files with timestamps."""
        self.daq_table = pd.read_csv(self.daq_file)
        self.stim_table = pd.read_csv(self.stim_file)
        if self.vitals_available:
            self.vitals_table = pd.read_csv(self.vitals_file, skiprows=1)
            self.vitals_table["i_sample"] = np.arange(self.vitals_table.shape[0])

    def print_samples(self):
        print("---Samples---")
        n_daq_samples = self.daq_table.shape[0]
        n_stim_samples = self.stim_table.shape[0]
        print(f"{n_daq_samples} daq samples")
        print(f"{n_stim_samples} stim samples")
        print(f"{self.n_tif_frames} tif frames.")
        if self.vitals_available:
            n_vitals_samples = self.vitals_table.shape[0]
            print(f"{n_vitals_samples} vitals samples")

    def rename_stim_columns(self) -> None:
        """Rename stim columns (for older files.)"""
        print(f"Renaming columns in flip table: {self.stim_columns_to_rename}")
        self.stim_table = self.stim_table.rename(columns=self.stim_columns_to_rename)

    def subtract_extra_start(self) -> None:
        """Subtract extra triggers collected at the start"""
        try:
            self.stim_table[self.frame_trigger_in_stim] += self.start_offset - 1
        except KeyError as ke:
            print(f"Columns of stim table: ")
            for col in self.stim_table.columns:
                print(f"\t {col}")
            raise ke
        self.daq_table[self.frame_trigger_in_daq] += self.start_offset - 1

    def subsample_daq(self) -> None:
        """Subsample DAQ csv to one row per frame."""
        print("---Subsampling DAQ to frame triggers---")
        is_selected = self.daq_table[f"interval_{self.frame_trigger_in_daq}"].notna()
        subsampled = self.daq_table.loc[is_selected, :].reset_index(drop=True)
        n_triggers = subsampled.shape[0]
        print(f"{n_triggers} frame triggers in labjack table.")
        self.daq_table = subsampled

    def check_triggers(self) -> None:
        """Check whether the python script registered every trigger that the labjack registered."""
        triggers = self.daq_table[self.frame_trigger_in_daq].values
        possible = np.arange(np.min(triggers), np.max(triggers))
        is_registered = np.isin(possible, triggers)
        is_missed = np.logical_not(is_registered)
        missed = possible[is_missed]
        n_missed = missed.size
        if n_missed > 0:
            print(f"{n_missed} triggers not registered: {missed}")
        else:
            print("All triggers registered.")

    def check_intervals(self) -> None:
        """Check the frame interval durations to spot suspicious triggers.."""
        self.print_interval_overview()
        self.print_first_last_intervals()
        self.print_extreme_intervals()

    def print_interval_overview(self) -> None:
        """Print min, median and max frame intervals."""
        all_intervals = self.daq_table[f"interval_{self.frame_trigger_in_daq}"].values
        median_interval = np.median(all_intervals)
        min_interval = np.min(all_intervals)
        max_interval = np.max(all_intervals)
        frame_rate = 1 / median_interval
        print(f"Intervals: min={min_interval * 1000:.1f}ms, median={median_interval * 1000:.1f}ms, max={max_interval * 1000:.1f}ms")
        print(f"Frame rate: {frame_rate:.1f} Hz")

    def print_first_last_intervals(self) -> None:
        """Print first and last 5 intervals."""
        for direction in [1, -1]:
            if direction == 1:
                print("---First intervals---")
            else:
                print("---Last intervals---")
            for i in range(5):
                if direction == -1 and i == 0:
                    continue
                row = self.daq_table.iloc[direction * i, :]
                trigger = row[self.frame_trigger_in_daq]
                interval = row[f"interval_{self.frame_trigger_in_daq}"]
                print(f"{trigger} -> {trigger + 1}: {interval * 1000:.1f} ms")

    def print_extreme_intervals(self) -> None:
        """Print longest and shortest intervals."""
        all_intervals = self.daq_table[f"interval_{self.frame_trigger_in_daq}"].values
        sort_indices = np.argsort(all_intervals)
        sorted_intervals = all_intervals[sort_indices]
        for direction in [-1, 1]:
            if direction == 1:
                print("---Shortest intervals---")
            else:
                print("---Longest intervals---")
            for i in range(5):
                if direction == -1 and i == 0:
                    continue
                interval = sorted_intervals[i * direction]
                index = sort_indices[i * direction]
                print(f"{index - 1} -> {index}: {interval * 1000:.3f} ms")

    def combine_daq_and_stim(self) -> None:
        """Combine labjack triggers and stim info."""
        print(f"---Finding stim info for each {self.recording_type} frame---")
        last_trigger = self.daq_table[self.frame_trigger_in_daq].max()
        all_frames = []
        for i_row, row in tqdm(self.daq_table.iterrows(), total=self.daq_table.shape[0]):
            frame_trigger = row[self.frame_trigger_in_daq]
            if frame_trigger < 0:
                print(f"Skipping trigger index {frame_trigger}: below 0.")
                continue
            elif (last_trigger - frame_trigger) < self.end_offset:
                print(f"Skipping trigger index {frame_trigger}: after end offset.")
                continue
            info_for_frame = self.process_single_frame(row)
            all_frames.append(info_for_frame)
        all_frames = pd.DataFrame(all_frames)
        self.frame_table = all_frames

    def process_single_frame(self, row: pd.Series) -> dict:
        """Process single recording frame: combine DAQ info with stim info"""
        daq_info_for_frame = self.get_daq_info_for_single_frame(row)
        stim_info_for_frame = self.get_stim_info_for_single_frame(row[self.frame_trigger_in_daq])
        info_for_frame = {**daq_info_for_frame, **stim_info_for_frame}
        if self.vitals_available:
            vitals_for_frame = self.get_vitals_for_frame(row)
            info_for_frame.update(vitals_for_frame)
        return info_for_frame

    def get_daq_info_for_single_frame(self, row: pd.Series) -> dict:
        frame_trigger = row[self.frame_trigger_in_daq]
        daq_info_for_frame = {
            f"i_{self.recording_type}_frame": frame_trigger,
            "datetime": row["datetime"],
            f"{self.recording_type}_frame_interval": row[f"interval_{self.frame_trigger_in_daq}"],
        }
        if isinstance(self.other_daq_triggers, list):
            for col in self.other_daq_triggers:
                daq_info_for_frame[f"i_{col}"] = row[col]
        return daq_info_for_frame

    def get_stim_info_for_single_frame(self, frame_trigger: int) -> dict:
        is_trigger = self.stim_table[self.frame_trigger_in_stim] == frame_trigger
        n_stim_flips = np.sum(is_trigger)
        stim_info_for_frame = {
            "stim_info_available": n_stim_flips > 0,
            f"n_stim_flips": n_stim_flips,
        }
        if n_stim_flips > 0:
            all_flips = self.stim_table.loc[is_trigger, :].to_dict(orient="records")
            first_flip = all_flips[0]
            stim_info_for_frame.update(first_flip)
        return stim_info_for_frame

    def get_vitals_for_frame(self, row: pd.Series) -> dict:
        vitals_trigger = row["vitals_monitor"]
        corresponding_sample = vitals_trigger // 10
        corresponding_sample = int(corresponding_sample)
        is_sample = self.vitals_table["i_sample"] == corresponding_sample
        n_samples = np.sum(is_sample)
        vitals_for_frame = {
            "vitals_info_available": n_samples > 0,
            f"n_vitals_samples": n_samples,
        }
        if n_samples > 0:
            vitals_for_frame["i_vitals_sample"] = self.vitals_table.loc[is_sample, "i_sample"].values[0]
            vitals_for_frame["breathing_rate"] = self.vitals_table.loc[is_sample, "Breathing Rate"].values[0]
            vitals_for_frame["heart_rate"] = self.vitals_table.loc[is_sample, "Heart Rate"].values[0]
        return vitals_for_frame

    def clean_up(self) -> None:
        """Remove unwanted columns"""
        for col in self.frame_table.columns:
            if "Unnamed" in col:
                del self.frame_table[col]

    def compare(self) -> None:
        n_frame_triggers = self.frame_table.shape[0]
        if n_frame_triggers == self.n_tif_frames:
            print(f"As many frame triggers as tif frames: {n_frame_triggers}")
        else:
            diff = n_frame_triggers - self.n_tif_frames
            if diff > 0:
                message = f"{diff} more triggers than tif frames."
            else:
                message = f"{-diff} more tif frames than triggers."
            warnings.warn(f"{n_frame_triggers=} != {self.n_tif_frames=}: {message}")