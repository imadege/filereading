from enum import Enum


class UploaderEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.name.lower(), cls))


class OutPutEnum(UploaderEnum):
    JSON = 1
    XML = 2


class FileType(UploaderEnum):
    CSV = 1
    EXCEL = 2
