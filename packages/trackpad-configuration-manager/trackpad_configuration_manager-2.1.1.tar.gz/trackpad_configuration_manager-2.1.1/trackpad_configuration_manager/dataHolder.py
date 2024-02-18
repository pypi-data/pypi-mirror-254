import io
import logging
import os
import shutil
from abc import abstractmethod
from enum import Enum

from PySide6.QtCore import Signal, QObject

from trackpad_configuration_manager.utils.crc16 import compute_crc


class DynamicDataSetType(Enum):
    WAVEFILE = 1
    BOS1921_REFERENCED_FEEDBACK = 2
    FILE_SYSTEM_FILE = 3


class DynamicDataSet:
    def __init__(self, data: bytes, data_type: DynamicDataSetType):
        self.data = data
        self.type = data_type

    def to_bytes(self) -> bytes:
        data = bytearray(self.type.value.to_bytes(length=1, byteorder="little", signed=False))  # data type
        data += bytearray(len(self.data).to_bytes(length=2, byteorder="little", signed=False))  # data length
        data += bytearray(self.data)  # data

        data += bytearray(compute_crc(data).to_bytes(length=2, byteorder="little", signed=False))  # crc

        return bytes(data)


class WavefileDataSet(DynamicDataSet):

    def __init__(self, data):
        super().__init__(data, DynamicDataSetType.WAVEFILE)


class FileSystemFileDataSet(DynamicDataSet):

    def __init__(self, data, device_file_path: str, path_length: int):
        super().__init__(data, DynamicDataSetType.FILE_SYSTEM_FILE)
        self.device_file_path = device_file_path
        self.path_length = path_length

    def to_bytes(self) -> bytes:
        data = bytearray(self.type.value.to_bytes(length=1, byteorder="little", signed=False))  # data type
        data += bytearray(
            len(self.device_file_path).to_bytes(length=2, byteorder="little", signed=False))  # Filepath length
        data += bytearray(self.device_file_path.encode())  # Filepath
        data += bytearray(len(self.data).to_bytes(length=2, byteorder="little", signed=False))  # data length
        data += bytearray(self.data)  # data
        data += bytearray(compute_crc(data).to_bytes(length=2, byteorder="little", signed=False))  # crc
        return bytes(data)


class DataHolder(QObject):
    updated_device_value = Signal(str, bool)

    def __init__(self):
        QObject.__init__(self)

    @abstractmethod
    def read_device_value(self, data: io.BytesIO):
        pass

    @abstractmethod
    def to_bytes(self) -> bytes:
        pass

    @abstractmethod
    def get_file_value(self):
        pass

    @abstractmethod
    def get_dynamic_memory_section(self) -> DynamicDataSet:
        pass


class BoolTypeDataHolder(DataHolder):
    def __init__(self, file_value: bool, is_read_only: bool = False):
        self._file_value = file_value
        self._device_value = 0
        self._device_bool = False
        self.length = 1
        self.is_read_only = is_read_only

        super().__init__()

    def read_device_value(self, data: io.BytesIO):
        self._device_value = int.from_bytes(data.read(self.length), byteorder="little", signed=False)

        if self._device_value == 1:
            self._device_bool = True
        elif self._device_value == 0:
            self._device_bool = False
        else:
            raise Exception("Invalid value")
        self.update_device_value_label()

    def to_bytes(self) -> bytes:
        value = 0

        if self._file_value:
            value = 1

        return value.to_bytes(length=self.length, byteorder="little", signed=False)

    def get_file_value(self):
        return self._file_value

    def get_file_value_int(self):
        if self._file_value:
            return 1

        return 0

    def get_device_value(self):
        return self._device_bool

    def get_device_str_value(self):
        return str(self._device_bool)

    def get_dynamic_memory_section(self) -> DynamicDataSet:
        pass

    def set_file_value(self, value: int):
        if value == 1:
            self._file_value = True
        elif value == 0:
            self._file_value = False
        else:
            raise Exception("Invalid value")
        self.update_device_value_label()

    def update_device_value_label(self):
        self.updated_device_value.emit(str(self._device_bool), self._device_bool != self._file_value)


class NativeTypeDataHolder(DataHolder):
    SUPPORTED_TYPE = {"uint8_t": {"signed": False, "length": 1, "min": 0, "max": 255},
                      "uint16_t": {"signed": False, "length": 2, "min": 0, "max": 65536},
                      "uint32_t": {"signed": False, "length": 4, "min": 0, "max": 4294967296},
                      "int8_t": {"signed": True, "length": 1, "min": -127, "max": 128},
                      "int16_t": {"signed": True, "length": 2, "min": -32767, "max": 32768},
                      "int32_t": {"signed": True, "length": 4, "min": -2147483647, "max": 2147483648}}

    DISPLAY_TYPE = {"hex", "bin", "dec"}

    def __init__(self, file_value: int, type: str, is_read_only, choices: dict = None, display_type: str = "dec"):
        self.type = type
        self._file_value = file_value
        self._device_value = 0
        self.is_read_only = is_read_only
        self.is_multiple_choice = False
        self.choices = None

        if len(display_type) > 0:
            if display_type not in self.DISPLAY_TYPE:
                raise Exception("Invalid display type")
            self.display_type = display_type
        else:
            self.display_type = "dec"

        if choices:
            self.is_multiple_choice = True
            self.choices = choices

        if type not in self.SUPPORTED_TYPE:
            raise Exception("Invalid type")

        super().__init__()

    def set_file_value(self, value: str):
        __value = 0

        match self.display_type:
            case "hex":
                # validate this is a valid hex string
                if not value.startswith("0x") or not value[2:].isalnum():
                    raise Exception("Invalid hex value")
                __value = int(value, 16)
            case "bin":
                if len(value) < 0 and value.isdigit() is False:
                    raise Exception("Invalid value")
                __value = int(value, 2)
            case "dec":
                if len(value) < 0 and value.isdigit() is False:
                    raise Exception("Invalid value")
                __value = int(value, 10)

        if __value < self.SUPPORTED_TYPE[self.type]["min"] or __value > self.SUPPORTED_TYPE[self.type]["max"]:
            raise Exception("out of range value")

        self._file_value = __value
        self.update_device_value_label()

    def set_file_value_from_int(self, value: int):
        if value < self.SUPPORTED_TYPE[self.type]["min"] or value > self.SUPPORTED_TYPE[self.type]["max"]:
            raise Exception("out of range value")

        self._file_value = value
        self.update_device_value_label()

    def set_file_value_from_choice(self, value: str):
        if not self.is_multiple_choice:
            raise Exception("Instance not multiple choices")

        if value not in self.choices:
            raise Exception("Invalid value")

        self._file_value = list(self.choices.keys()).index(value)
        self.update_device_value_label()

    def get_file_value(self) -> int:
        return self._file_value

    def get_file_str_value(self) -> str:
        return self.__convert_value_str(self._file_value)

    def get_file_str_value_from_choice(self) -> str:
        if self.is_multiple_choice:
            for choice, value in self.choices.items():
                if value == self._file_value:
                    return choice

            raise Exception("No corresponding choice")
        raise Exception("Instance not multiple choices")

    def get_file_index_from_choice(self) -> int:
        if self.is_multiple_choice:
            index = 0
            for choice, value in self.choices.items():
                if value == self._file_value:
                    return index
                index += 1
            raise Exception("No corresponding choice")
        raise Exception("Instance not multiple choices")

    def get_device_value(self) -> int:
        return self._device_value

    def get_device_str_value_from_choice(self) -> str:
        if self.is_multiple_choice:
            for choice, value in self.choices.items():
                if value == self._device_value:
                    return choice

            raise Exception("No corresponding choice")
        raise Exception("Instance not multiple choices")

    def get_choices_str(self):
        str_choices = []

        for choice in self.choices:
            str_choices.append(choice)

        return str_choices

    def __convert_value_str(self, value: int) -> str:
        match self.display_type:
            case "hex":
                return "0x" + hex(value)[2:].upper().zfill(self.SUPPORTED_TYPE[self.type]["length"])
            case "bin":
                # return a string with 0b prefix
                return "0b" + bin(value)[2:].zfill(self.SUPPORTED_TYPE[self.type]["length"] * 8)
            case "dec":
                return str(value)

    def get_device_str_value(self) -> str:
        return self.__convert_value_str(self._device_value)

    def to_bytes(self) -> bytes:
        return self._file_value.to_bytes(length=self.SUPPORTED_TYPE[self.type]["length"], byteorder="little",
                                         signed=self.SUPPORTED_TYPE[self.type]["signed"])

    def read_device_value(self, data: io.BytesIO):
        length = self.SUPPORTED_TYPE[self.type]["length"]

        self._device_value = int.from_bytes(data.read(length), byteorder="little",
                                            signed=self.SUPPORTED_TYPE[self.type]["signed"])
        self.update_device_value_label()

    def get_dynamic_memory_section(self) -> DynamicDataSet:
        pass

    def update_device_value_label(self):
        str_device_value = self.get_device_str_value_from_choice() if self.is_multiple_choice else self.get_device_str_value()
        self.updated_device_value.emit(str_device_value, self._device_value != self._file_value)


class WaveFile:
    def __init__(self, name, path):
        self.name = name
        self.path = path


class DynamicSectionNotFoundException(Exception):
    def __init__(self, path: str):
        self.path = path
        super().__init__("Cannot find dynamic section at : " + path)


class WavefileDataHolder(DataHolder):

    def get_device_str_value(self):
        pass

    def __init__(self, file_value: dict, base_location: str):
        self.on_file = WaveFile(file_value["name"], file_value["local-path"])
        self.on_device = WaveFile(file_value["name"], file_value["local-path"])
        if file_value.get("length-name") is None:
            self.length_name = 0
        else:
            self.length_name = file_value["length-name"]
        if file_value.get("length-path") is None:
            self.length_path = 0
        else:
            self.length_path = file_value["length-path"]
        self.base_location = os.path.dirname(os.path.abspath(base_location))
        self.path_device = "ramfs:/" + self.on_file.name

        super().__init__()

    def update_on_file(self, file_path: str):

        if self.base_location not in file_path:
            # if there is already a file with the same name, remove it
            if os.path.exists(os.path.join(self.base_location, os.path.basename(file_path))):
                os.remove(os.path.join(self.base_location, os.path.basename(file_path)))

            # copy file to the base location in the resources folder
            shutil.copy(file_path, self.base_location)
            file_path = os.path.join(self.base_location, os.path.basename(file_path))

        self.on_file.path = os.path.relpath(file_path, self.base_location)
        self.on_file.name = os.path.basename(file_path)
        self.update_device_value_label()

    def get_full_path_on_file(self) -> str:
        return self.on_file.path

    def read_device_value(self, data: io.BytesIO):
        name_data = data.read(self.length_name)

        path_data = data.read(self.length_path)

        try:
            self.on_device.name = name_data.decode('ascii').strip().strip('\x00')
            self.on_device.path = path_data.decode('ascii').strip().strip('\x00')
        except Exception as error:
            logging.info(str(error))

        self.update_device_value_label()

    def to_bytes(self) -> bytes:

        byte_array = bytearray(self.on_file.name.encode())
        byte_array += bytearray(self.length_name - len(self.on_file.name))

        path_device = "ramfs:/" + self.on_file.name
        byte_array += bytearray(path_device.encode())
        byte_array += bytearray(self.length_path - len(path_device))

        return bytes(byte_array)

    def get_file_value(self):
        file_value = dict()

        file_value["length-name"] = self.length_name
        file_value["name"] = self.on_file.name
        file_value["length-path"] = self.length_path
        file_value["local-path"] = self.on_file.path

        return file_value

    def get_dynamic_memory_section(self) -> DynamicDataSet:

        try:
            file_desc = open(self.base_location + "\\" + self.on_file.path, "rb")
            data = file_desc.read()
        except Exception:
            raise DynamicSectionNotFoundException(self.base_location + "\\" + self.on_file.path)

        return WavefileDataSet(data)

    def update_device_value_label(self):
        # FIXME Not sure how to handle the modification status here...
        self.updated_device_value.emit(self.on_device.path, False)


class FileSystemDataHolder(WavefileDataHolder):
    def __init__(self, file_value: dict, base_location: str):
        super().__init__(file_value, base_location)

    def to_bytes(self) -> bytes:
        return bytes()

    def get_dynamic_memory_section(self) -> DynamicDataSet:
        if len(self.on_file.path) > 0:
            data = bytearray()
            try:
                file_desc = open(self.base_location + "\\" + self.on_file.path, "rb")
                data = file_desc.read()
            except Exception:
                raise DynamicSectionNotFoundException(self.base_location + "\\" + self.on_file.path)
            return FileSystemFileDataSet(data, self.path_device, self.length_path)
        else:
            pass


class StringDataHolder(DataHolder):

    def __init__(self, file_value: dict, is_read_only: bool = False):
        super().__init__()
        self.string = file_value["value"]
        self.maximum_length = file_value["maximum-length"]
        self.on_device_string = ""
        self.is_read_only = is_read_only

    def get_dynamic_memory_section(self) -> DynamicDataSet:
        pass

    def get_file_value(self):
        file_value = dict()

        file_value["maximum-length"] = self.maximum_length
        file_value["value"] = self.string

        return file_value

    def to_bytes(self) -> bytes:
        byte_array = bytearray(self.string.encode())
        byte_array += bytearray(self.maximum_length - len(self.string))
        return bytes(byte_array)

    def set_file_value(self, string):
        self.string = string
        self.update_on_device_string()

    def read_device_value(self, data: io.BytesIO):

        string = data.read(self.maximum_length)

        try:
            self.on_device_string = string.decode('ascii').strip().strip('\x00')
            self.update_on_device_string()
        except Exception as error:
            logging.info(str(error))

    def update_on_device_string(self):
        self.updated_device_value.emit(self.on_device_string, self.on_device_string != self.string)
