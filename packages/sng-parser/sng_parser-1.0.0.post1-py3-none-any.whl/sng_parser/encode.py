import io
import os

from configparser import ConfigParser
from typing import List, Optional


from .common import (
    write_uint32,
    write_uint8,
    write_uint64,
    mask,
    SngFileMetadata,
    SngMetadataInfo,
)


def write_header(file: io.FileIO, version: int, xor_mask: bytes) -> None:
    file.write(b"SNGPKG")
    write_uint32(file, version)
    file.write(xor_mask)


def write_file_meta(file: io.FileIO, file_meta_array: List[SngFileMetadata]) -> None:
    file_meta_length = sum(
        1 + len(meta.filename.encode("utf-8")) + 16 for meta in file_meta_array
    )
    write_uint64(file, file_meta_length)
    write_uint64(file, len(file_meta_array))

    for file_meta in file_meta_array:
        filename_bytes = file_meta.filename.encode("utf-8")

        write_uint8(file, len(filename_bytes))
        file.write(filename_bytes)

        write_uint64(file, file_meta.content_len)
        write_uint64(file, file_meta.content_idx)


def write_metadata(file: io.FileIO, metadata: SngMetadataInfo) -> None:
    metadata_content = bytearray()

    for key, value in metadata.items():
        key_bytes = key.encode("utf-8")
        value_bytes = value.encode("utf-8")

        write_uint32(metadata_content, len(key_bytes))
        metadata_content += key_bytes

        write_uint32(metadata_content, len(value_bytes))
        metadata_content += value_bytes

    write_uint64(file, len(metadata_content))
    write_uint64(file, len(metadata))
    file.write(metadata_content)


def write_file_data(file: io.FileIO, file_data_array: List[bytearray], xor_mask: bytes):
    total_file_data_length = sum(len(data) for data in file_data_array)
    write_uint64(file, total_file_data_length)

    for data in file_data_array:
        masked_data = mask(data, xor_mask)
        file.write(masked_data)


def to_sng_file(
    output_filename: os.PathLike,
    directory: os.PathLike,
    version: int = 1,
    xor_mask: Optional[bytes] = None,
    metadata: Optional[SngMetadataInfo] = None,
) -> None:
    if metadata is None:
        metadata = read_file_meta(directory)
    if xor_mask is None:
        xor_mask = os.urandom(16)

    with open(output_filename, "wb") as file:
        write_header(file, version, xor_mask)
        write_metadata(file, metadata)
        file_meta_array, file_data_array = gather_files_from_directory(directory)
        write_file_meta(file, file_meta_array)
        write_file_data(file, file_data_array, xor_mask)


def gather_files_from_directory(directory: os.PathLike):
    file_meta_array = []
    file_data_array = []
    current_index = 0

    for filename in os.listdir(directory):
        if filename == "song.ini":
            continue

        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, "rb") as file:
                file_data = file.read()

            file_meta = SngFileMetadata(filename, len(file_data), current_index)
            print(file_meta)
            file_meta_array.append(file_meta)
            file_data_array.append(file_data)

            current_index += len(file_data)

    return file_meta_array, file_data_array


def read_file_meta(filedir: os.PathLike) -> SngMetadataInfo:
    cfg = ConfigParser()
    with open(os.path.join(filedir, "song.ini")) as f:
        cfg.read_file(f)
    return dict(cfg["Song"])
