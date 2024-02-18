"""Read a leica <name>_Properties.xml file."""
from pathlib import Path
import datetime

import pandas as pd
from tqdm import tqdm


RELATIVE_PATTERN = '(?<=RelativeTime=")[0-9]+\.[0-9]+'


def read_xml_file(file_path: Path) -> pd.DataFrame:
    """
    Converts a local leica .xml file into a pandas.DataFrame.
    Main function to call.
    """
    with open(file_path, mode="r") as file:
        lines = file.readlines()
    timestamps = extract_timestamps_from_lines(lines)
    return timestamps


def extract_timestamps_from_lines(lines: list[str]) -> pd.DataFrame:
    """Find timestamp lines and extract to pd.DataFrame"""
    timestamp_section: str = find_timestamp_section(lines)
    potential_timestamps: list[str] = timestamp_section.split("<")

    list_of_timestamps = []
    count = 0

    print(f"XML reader: Attempting to read {len(potential_timestamps)} timestamp-related lines.")
    for potential_timestamp in tqdm(potential_timestamps):
        if "RelativeTime" in potential_timestamp:
            components: dict[str, str] = extract_components_from_timestamp(potential_timestamp)
            components = convert_components_to_datetime(components)
            single_timestamp = {
                "i_frame": count,
                "relative_time": components["relative_time"],
                "datetime": components["datetime"],
            }
            list_of_timestamps.append(single_timestamp)
            count += 1
    timestamps = pd.DataFrame(list_of_timestamps)
    print(f"XML reader: Found {timestamps.shape[0]} timestamps.")
    return timestamps


def find_timestamp_section(lines: list[str]) -> str:
    """Find single line in XML file that contains all frame timestamps"""
    timestamp_line = None
    for line in lines:
        if "TimeStamp" in line:
            timestamp_line = line
            break
    if timestamp_line is None:
        raise ValueError("Cannot find timestamp line in lines.")
    return timestamp_line


def extract_components_from_timestamp(timestamp: str) -> dict[str, str]:
    """Extract timestamp information."""
    parts = timestamp.split('"')
    components = {
        "relative_time": parts[1],
        "date": parts[3],
        "time": parts[5],
        "milliseconds": parts[7],
    }
    return components


def convert_components_to_datetime(timing: dict) -> dict:
    """Convert timestamp information to make uniform."""
    relative_time = float(timing["relative_time"])
    date_object: datetime.datetime = datetime.datetime.strptime(timing["date"], "%Y-%m-%d")
    date_object: datetime.date = date_object.date()
    time_object: datetime.datetime = datetime.datetime.strptime(timing["time"], "%I:%M:%S %p")
    milliseconds = float(timing["milliseconds"])
    time_object = time_object + datetime.timedelta(milliseconds=milliseconds)
    time_object: datetime.time = time_object.time()
    dt = datetime.datetime.combine(date_object, time_object)
    timing = {
        "relative_time": relative_time,
        "datetime": dt,
    }
    return timing
