from __future__ import annotations

import datetime
import struct
import zlib
from collections.abc import Buffer
from dataclasses import dataclass

LOCAL_FILE_HEADER_SIGNATURE = 0x04034B50
CENTRAL_FILE_HEADER_SIGNATURE = 0x02014B50
END_OF_CENTRAL_DIR_SIGNATURE = 0x06054B50
ZIP_VERSION_2 = 20
FLAG_DATA_DESCRIPTOR = 1 << 3
FLAG_LANGUAGE_ENCODING = 1 << 11
COMPRESSION_NONE = 0
SUPPLIED_IN_DATA_DESCRIPTOR = 0
DISK_0 = 0
INTERNAL_FILE_ATTRIBUTES = 0
EXTERNAL_FILE_ATTRIBUTES = 0


def date_to_msdos(date: datetime.date):
    if 1980 <= date.year <= 2107:
        return ((date.year - 1980) << 9) | (date.month << 5) | (date.day)
    raise ValueError("Year is out of supported range")


def time_to_msdos(time: datetime.time):
    return (time.hour << 11) | (time.minute << 5) | (time.second // 2)


def local_header_offset(entry: FileHeader, entries: list[FileHeader]):
    offset = 0
    for e in entries:
        if entry is e:
            return offset

        offset += e.file_header_data_descriptor_size()

    raise ValueError("File header was not found in entries")


@dataclass
class FileHeader:
    last_mod_file_time: datetime.time  # 2
    last_mod_file_date: datetime.date  # 2
    crc32: int  # 4
    compressed_size: int  # 4
    uncompressed_size: int  # 4
    file_name: str  # 2
    extra_field: bytes  # 2
    file_comment: str  # 2

    def local_header(self):
        file_name_bytes = self.file_name.encode()
        bytes = struct.pack(
            "<IHHHHHIIIHH",
            LOCAL_FILE_HEADER_SIGNATURE,
            ZIP_VERSION_2,
            FLAG_DATA_DESCRIPTOR | FLAG_LANGUAGE_ENCODING,
            COMPRESSION_NONE,
            time_to_msdos(self.last_mod_file_time),
            date_to_msdos(self.last_mod_file_date),
            SUPPLIED_IN_DATA_DESCRIPTOR,
            SUPPLIED_IN_DATA_DESCRIPTOR,
            SUPPLIED_IN_DATA_DESCRIPTOR,
            len(file_name_bytes),
            len(self.extra_field),
        )
        return bytes + file_name_bytes + self.extra_field

    def local_header_size(self):
        file_name_bytes = self.file_name.encode()
        return 30 + len(file_name_bytes) + len(self.extra_field)

    def update_crc32(self, chunk: Buffer):
        self.crc32 = zlib.crc32(chunk, self.crc32)

    def data_descriptor(self):
        return struct.pack(
            "<III", self.crc32, self.compressed_size, self.uncompressed_size
        )

    def file_header_data_descriptor_size(self):
        return self.local_header_size() + self.compressed_size + 12

    def central_directory_header(self, entries: list[FileHeader]):
        file_name_bytes = self.file_name.encode()
        file_comment_bytes = self.file_comment.encode()
        bytes = struct.pack(
            "<IHHHHHHIIIHHHHHII",
            CENTRAL_FILE_HEADER_SIGNATURE,
            ZIP_VERSION_2,
            ZIP_VERSION_2,
            FLAG_DATA_DESCRIPTOR | FLAG_LANGUAGE_ENCODING,
            COMPRESSION_NONE,
            time_to_msdos(self.last_mod_file_time),
            date_to_msdos(self.last_mod_file_date),
            self.crc32,
            self.compressed_size,
            self.uncompressed_size,
            len(file_name_bytes),
            len(self.extra_field),
            len(file_comment_bytes),
            DISK_0,
            INTERNAL_FILE_ATTRIBUTES,
            EXTERNAL_FILE_ATTRIBUTES,
            local_header_offset(self, entries),
        )
        return bytes + file_name_bytes + self.extra_field + file_comment_bytes

    def central_directory_header_size(self):
        file_name_bytes = self.file_name.encode()
        file_comment_bytes = self.file_comment.encode()
        return (
            46 + len(file_name_bytes) + len(self.extra_field) + len(file_comment_bytes)
        )


def end_of_central_directory(entries: list[FileHeader], zip_file_comment: str = ""):
    central_directory_size = sum(e.central_directory_header_size() for e in entries)
    central_directory_offset = sum(
        e.file_header_data_descriptor_size() for e in entries
    )
    zip_file_comment_bytes = zip_file_comment.encode()
    bytes = struct.pack(
        "<IHHHHIIH",
        END_OF_CENTRAL_DIR_SIGNATURE,
        DISK_0,
        DISK_0,
        len(entries),
        len(entries),
        central_directory_size,
        central_directory_offset,
        len(zip_file_comment_bytes),
    )
    return bytes + zip_file_comment_bytes


def end_of_central_directory_size(zip_file_comment: str = ""):
    zip_file_comment_bytes = zip_file_comment.encode()
    return 22 + len(zip_file_comment_bytes)


def zip_file_size(entries: list[FileHeader], zip_file_comment: str = ""):
    return sum(
        e.file_header_data_descriptor_size() + e.central_directory_header_size()
        for e in entries
    ) + end_of_central_directory_size(zip_file_comment)
