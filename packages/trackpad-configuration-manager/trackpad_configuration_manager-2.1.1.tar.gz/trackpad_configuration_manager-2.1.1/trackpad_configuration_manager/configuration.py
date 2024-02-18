import copy
import io
import json
import os

from PySide6.QtCore import QObject, Signal

from trackpad_configuration_manager.Bos1921Dataholder import Bos1921WavefileDataHolder
from trackpad_configuration_manager.dataHolder import NativeTypeDataHolder, WavefileDataHolder, DataHolder, \
    StringDataHolder, FileSystemDataHolder, BoolTypeDataHolder
from trackpad_configuration_manager.marshaller import ConfMarshaller
from trackpad_configuration_manager.probe.probe import Probe
from trackpad_configuration_manager.utils.execUtils import resource_path
from trackpad_configuration_manager.utils.hexFile import HexFile
from view.MessageDialog import ErrorMessageDialog


def remove_error_info(d):
    if not isinstance(d, (dict, list)):
        return d
    if isinstance(d, list):
        return [remove_error_info(v) for v in d]
    return {k: remove_error_info(v) for k, v in d.items()
            if k not in {'errMsg', 'errCode'}}


class CRC(QObject):
    updated_crc_on_device = Signal(int, bool)
    updated_crc_on_file = Signal(int)

    def __init__(self):
        QObject.__init__(self)
        self._on_device = 0
        self._in_file = 0

    def set_crc_on_device(self, crc: int):
        self._on_device = crc
        self.updated_crc_on_device.emit(self._on_device, self._on_device == self._in_file)

    def set_crc_in_file(self, crc: int):
        self._in_file = crc
        self.updated_crc_on_file.emit(self._in_file)
        self.updated_crc_on_device.emit(self._on_device, self._on_device == self._in_file)


class BaseConfigFile:

    CRC_SIZE = 2

    def __init__(self, json_data: dict, file_path: str, name: str):
        self.json_data = json_data
        self.file_path = file_path
        self.device_address = json_data["target_address"]["value"]
        self.target_device = json_data["target_cpu"]["value"]

        if "target_space" in json_data:
            self.total_memory_available = json_data["target_space"]["value"]
        else:
            self.total_memory_available = 0

        self.name = name

        self._crc_on_device = 0
        self.trackpad_conf = ConfMarshaller(self.json_data)

        self.__add_on_device_value(self.json_data, io.BytesIO())
        self.crc = CRC()

    def read_device_data(self, probe: Probe) -> dict():
        binary, crc = self.trackpad_conf.get_binary_for_static_memory()
        self.crc.set_crc_in_file(crc)
        length = len(binary)

        data = probe.read_data(int(self.device_address, 16), length)
        byte_io = io.BytesIO(data)

        self.crc.set_crc_on_device(int.from_bytes(byte_io.read(BaseConfigFile.CRC_SIZE), byteorder="little"))

        try:
            self.__add_on_device_value(self.json_data, byte_io)
        except Exception:
            ErrorMessageDialog("Failed to parse data received from device").show()

    def get_file_data(self) -> dict():
        return self.json_data

    def get_memory_footprint(self) -> int:

        binary, crc = self.trackpad_conf.get_binary_for_static_memory()
        dynamic_binary = self.trackpad_conf.get_binaries_for_dynamic_memory()

        return len(binary) + len(dynamic_binary)

    def __get_binary(self) -> bytearray:
        binary, crc = self.trackpad_conf.get_binary_for_static_memory()
        dynamic_binary = self.trackpad_conf.get_binaries_for_dynamic_memory()

        return binary + dynamic_binary

    def save_on_device(self, probe: Probe):

        try:
            file_name = resource_path("conf.bin")
            file_binary = open(file_name, "wb")
            binary, crc = self.trackpad_conf.get_binary_for_static_memory()
            dynamic_binary = self.trackpad_conf.get_binaries_for_dynamic_memory()
            self.crc.set_crc_in_file(crc)
            file_binary.write(binary)

            if len(dynamic_binary) > 0:
                file_binary.write(dynamic_binary)

            file_binary.close()
            probe.write_data_from_file(file_name, int(self.device_address, 16))
        finally:
            os.remove(file_name)

    def get_hex_file(self) -> HexFile:
        return HexFile(self.__get_binary(), int(self.device_address, 0), self.name)

    def save_to_bin_file(self, file_name: str):
        with open(file_name, "wb") as file:
            file.write(self.__get_binary())

    def save_to_hex_file(self, hex_file_path: str):
        hex_file = self.get_hex_file()
        hex_file.generate_file(hex_file_path)

    @staticmethod
    def __handle_array_list_device_data(data_list: list, data: io.BytesIO):

        value_list = data_list["value"]
        for row in range(len(value_list)):
            for col in range(len(value_list[row])):

                if not isinstance(value_list[row][col], NativeTypeDataHolder):
                    value_list[row][col] = NativeTypeDataHolder(value_list[row][col], data_list["type"], False)

                value_list[row][col].read_device_value(data)

    def __add_on_device_value(self, d, data: io.BytesIO):

        if not isinstance(d, (dict, list)):
            return
        if isinstance(d, list):
            for v in d:
                self.__add_on_device_value(v, data)
        else:
            if "type" in d:
                match d["type"]:
                    case ("uint8_t" | "uint16_t" | "uint32_t" | "int8_t" | "int16_t" | "int32_t"):
                        # handle array list
                        if isinstance(d["value"], list):
                            self.__handle_array_list_device_data(d, data)
                        else:
                            if not isinstance(d["value"], NativeTypeDataHolder):
                                is_read_only = False
                                display_type = str()
                                choices = None

                                if "is_read_only" in d:
                                    is_read_only = d["is_read_only"]
                                if "display_type" in d:
                                    display_type = d["display_type"]
                                if "choices" in d:
                                    choices = d["choices"]

                                d["value"] = NativeTypeDataHolder(int(d["value"]), d["type"], is_read_only,
                                                                  choices, display_type)
                            d["value"].read_device_value(data)
                    case "string-wavefile-name-path":
                        if not isinstance(d["value"], WavefileDataHolder):
                            d["value"] = WavefileDataHolder(d["value"], self.file_path)
                        d["value"].read_device_value(data)
                    case "bos1921-referenced-wavefile":
                        if not isinstance(d["value"], Bos1921WavefileDataHolder):
                            d["value"] = Bos1921WavefileDataHolder(d["value"], self.file_path)
                        d["value"].read_device_value(data)
                    case "filesystem-file":
                        if not isinstance(d["value"], FileSystemDataHolder):
                            d["value"] = FileSystemDataHolder(d["value"], self.file_path)
                        d["value"].read_device_value(data)
                    case "string":
                        if not isinstance(d["value"], StringDataHolder):
                            is_read_only = False
                            if "is_read_only" in d:
                                is_read_only = d["is_read_only"]
                            d["value"] = StringDataHolder(d["value"], is_read_only)
                        d["value"].read_device_value(data)
                    case "bool":
                        if not isinstance(d["value"], BoolTypeDataHolder):
                            is_read_only = False
                            if "is_read_only" in d:
                                is_read_only = d["is_read_only"]
                            d["value"] = BoolTypeDataHolder(d["value"], is_read_only)
                        d["value"].read_device_value(data)

            for key, value in d.items():
                self.__add_on_device_value(value, data)

    def save_on_file(self, file_path: str = None):

        configuration_to_file = copy.copy(self.json_data)

        for key, element in configuration_to_file.items():
            configuration_to_file[key] = self._remove_data_holder(element)

        output_string = json.dumps(configuration_to_file, indent=4)

        if file_path is None:
            file_path = self.file_path

        with open(file_path, 'w') as outfile:
            outfile.write(output_string)

    def _remove_data_holder(self, element):
        if not isinstance(element, (dict, list)):
            return element
        if isinstance(element, list):
            list_json = list()
            for v in element:
                if isinstance(v, DataHolder):
                    list_json.append(v.get_file_value())
                else:
                    list_json.append(self._remove_data_holder(v))

            return list_json

        dict_json = dict()

        for k, v in element.items():
            if isinstance(v, DataHolder):
                dict_json[k] = v.get_file_value()
            else:
                dict_json[k] = self._remove_data_holder(v)

        return dict_json


class Calibration(BaseConfigFile):
    def __init__(self, json_data: dict, file_path: str):
        super(Calibration, self).__init__(json_data, file_path, "calibration")


class Configuration(BaseConfigFile):
    def __init__(self, json_data: dict, file_path: str):
        super(Configuration, self).__init__(json_data, file_path, "configuration-ux")
