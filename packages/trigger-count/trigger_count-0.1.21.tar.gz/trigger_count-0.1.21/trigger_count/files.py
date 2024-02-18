from pathlib import Path

import tifffile


def get_n_frames(file_path: Path) -> int:
    """Get number of frames of a .tif without loading file into memory."""
    file = tifffile.TiffFile(file_path)
    n_frames = len(file.pages)
    if n_frames == 1:
        n_frames = file.imagej_metadata["images"]
    return n_frames
