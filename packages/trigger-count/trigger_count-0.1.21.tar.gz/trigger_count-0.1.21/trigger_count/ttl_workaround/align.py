"""Solve ttl_workaround for leica camera which does not send or receive triggers."""

import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from tqdm import tqdm

from trigger_count.ttl_workaround.xml import read_xml_file


class TtlTimestampAligner:
    def __init__(
            self,
            ttl_datetime_format: str,
            ttl_datetime_column: str,
            ttl_count_column: str,
            stim_frame_column: str,
            stim_count_column: str,
            stim_columns_to_extract: list,

    ) -> None:
        self.ttl_datetime_format: str = ttl_datetime_format
        self.ttl_datetime_column: str = ttl_datetime_column
        self.ttl_count_column: str = ttl_count_column
        self.stim_frame_column: str = stim_frame_column
        self.stim_count_column: str = stim_count_column
        self.stim_columns_to_extract: list = stim_columns_to_extract

    def run(self, path_to_xml: Path, path_to_stim: Path, path_to_ttl: Path) -> pd.DataFrame:
        """Main method to call."""
        # read
        leica_timestamps = self.read_xml(path_to_xml)
        stim_timestamps = pd.read_csv(path_to_stim)
        ttl_timestamps = pd.read_csv(path_to_ttl)

        print(f"Earliest leica timestamp: {leica_timestamps['datetime'].min()}")
        print(f"Last leica timestamp: {leica_timestamps['datetime'].max()}")
        print(f"Earliest TTL timestamp: {ttl_timestamps[self.ttl_datetime_column].min()}")
        print(f"Last TTL timestamp: {ttl_timestamps[self.ttl_datetime_column].max()}")

        # combine
        ttl_timestamps = self.add_wf_frames_to_ttl(ttl_timestamps, leica_timestamps)
        stim_timestamps = self.add_wf_frames_to_stim(stim_timestamps, ttl_timestamps)
        leica_timestamps = self.add_stim_to_wf_frames(leica_timestamps, stim_timestamps)
        return leica_timestamps

    @staticmethod
    def read_xml(path_to_xml: Path) -> pd.DataFrame:
        """Read a leica <name>_Properties.xml file."""
        leica_timestamps = read_xml_file(path_to_xml)
        return leica_timestamps

    def add_wf_frames_to_ttl(self, ttl_timestamps: pd.DataFrame, leica_timestamps: pd.DataFrame) -> pd.DataFrame:
        """Add widefield frames to ttl pulses via local computer clock timings."""
        print(f"Finding a widefield frame ({leica_timestamps.shape[0]}) for each outgoing TTL pulse ({ttl_timestamps.shape[0]}).")
        widefield_frames = []
        offsets = []
        ttl_timestamps["datetime"] = [datetime.datetime.strptime(x, self.ttl_datetime_format) for x in ttl_timestamps[self.ttl_datetime_column]]
        for i_row, pulse_row in tqdm(ttl_timestamps.iterrows(), total=ttl_timestamps.shape[0]):
            deviations = leica_timestamps["datetime"] - pulse_row["datetime"]
            minimum_deviation: pd.Timedelta = np.min(np.abs(deviations))
            minimum_deviation: float = minimum_deviation.total_seconds()
            index_of_min = np.argmin(np.abs(deviations))
            frame = leica_timestamps["i_frame"].values[index_of_min]
            widefield_frames.append(frame)
            offsets.append(minimum_deviation)
        ttl_timestamps["i_widefield_frame"] = widefield_frames
        ttl_timestamps["widefield_frame_pulse_offset"] = offsets
        return ttl_timestamps

    def add_wf_frames_to_stim(self, stim_timestamps: pd.DataFrame, ttl_timestamps: pd.DataFrame) -> pd.DataFrame:
        """Add widefield frames to stim frames via TTL pulse counts."""
        print("Aligning outgoing and incoming pulses.")

        # rename for consistency
        ttl_timestamps = ttl_timestamps.rename(columns={self.ttl_count_column: "pulse_count"})
        stim_timestamps = stim_timestamps.rename(
            columns={
                self.stim_frame_column: "i_stim_frame",
                self.stim_count_column: "pulse_count",
            }
        )

        # report pulse info
        df_per_name = {"Pulse sender (WF)": ttl_timestamps, "Pulse receiver (stim)": stim_timestamps}
        for name, df in df_per_name.items():
            print(name)
            n_pulses = df["pulse_count"].nunique()
            min_count = df["pulse_count"].min()
            max_count = df["pulse_count"].max()
            print(f"{name}: {min_count=}, {max_count=}, {n_pulses=}")

        # align
        print(f"Finding a pulse and widefield frame for each stim frame ({stim_timestamps.shape[0]}).")
        widefield_frames = []
        for i_row, stim_row in tqdm(stim_timestamps.iterrows(), total=stim_timestamps.shape[0]):
            stim_pulse = stim_row["pulse_count"]
            is_pulse = ttl_timestamps["pulse_count"] == stim_pulse
            n_selected = np.sum(is_pulse)
            if n_selected > 0:
                i_wf_frame = ttl_timestamps.loc[is_pulse, "i_widefield_frame"].values[0]
                widefield_frames.append(i_wf_frame)
            else:
                print(f"Incoming pulse count {stim_pulse} does not exist in outgoing pulses.")
                widefield_frames.append(None)
        stim_timestamps["i_widefield_frame"] = widefield_frames
        return stim_timestamps

    def add_stim_to_wf_frames(self, leica_timestamps: pd.DataFrame, stim_timestamps: pd.DataFrame) -> pd.DataFrame:
        """Add stim info to widefield frames."""
        print(f"Finding stim info for every widefield frame ({leica_timestamps.shape[0]})")
        stim_info = []
        leica_timestamps = leica_timestamps.rename(columns={"i_frame": "i_widefield_frame", "dt": "widefield_datetime"})

        for i_row, frame_row in tqdm(leica_timestamps.iterrows(), total=leica_timestamps.shape[0]):
            is_frame = stim_timestamps["i_widefield_frame"] == frame_row["i_widefield_frame"]
            if np.sum(is_frame) < 1:
                info = {col: None for col in self.stim_columns_to_extract}
                stim_info.append(info)
            else:
                stim_frames_for_widefield_frame = stim_timestamps.loc[is_frame, :]
                info = {col: stim_frames_for_widefield_frame[col].values[0] for col in self.stim_columns_to_extract}
                stim_info.append(info)

        stim_info = pd.DataFrame(stim_info)
        leica_timestamps = pd.concat([leica_timestamps, stim_info], axis=1)
        return leica_timestamps
