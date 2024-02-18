from trackpad_configuration_manager.dataHolder import DataHolder
from trackpad_configuration_manager.utils.crc16 import compute_crc


def process_struct(element: dict) -> bytearray():
    data = bytearray()
    for key, value in element.items():
        data += process_type(value)

    return data


def process_value(data_holder: DataHolder) -> bytearray():
    data = None

    if isinstance(data_holder, DataHolder):
        data = data_holder.to_bytes()
    else:
        data = bytes()

    return bytearray(data)


def process_value_array_proxy(element) -> bytearray():
    data = bytearray()
    if isinstance(element, list):
        for value in element:
            data += process_value(value)
    else:
        data += process_value(element)
    return data


def process_value_array(array_value: list, _type: str) -> bytearray():
    data = bytearray()
    for value in array_value:
        match _type:
            case "struct":
                data += process_struct(value)
            case _:
                data += process_value_array_proxy(value)
    return data


def process_type(element: dict) -> bytearray():
    data = bytearray()
    if "type" in element and "value" in element:
        if isinstance(element["value"], DataHolder):
            data = process_value(element["value"])
        elif isinstance(element["value"], dict):
            data = process_struct(element["value"])
        elif isinstance(element["value"], list):
            data = process_value_array(element["value"], element["type"])

    return data


def generate_binary(dict_json: dict) -> bytearray():
    data = bytearray()
    for key, value in dict_json.items():
        data += process_type(value)

    return data


class ConfMarshaller:
    def __init__(self, json_head_struct: dict):

        if "version" not in json_head_struct:
            raise Exception("Json dict doesn't contains mandatory version element")

        self.data_on_file = json_head_struct

    def get_binary_for_static_memory(self) -> [bytearray(), int]:
        data = generate_binary(self.data_on_file)

        checksum = compute_crc(data)
        crc_byte = checksum.to_bytes(length=2, byteorder="little", signed=False)

        return bytearray(crc_byte) + data, checksum

    def __get_all_dynamic_data_set(self, d) -> list:
        list_data_set = list()

        if isinstance(d, DataHolder):
            return [d.get_dynamic_memory_section()]
        if not isinstance(d, (dict, list)):
            return list()
        if isinstance(d, list):
            for v in d:
                list_data_set += self.__get_all_dynamic_data_set(v)
            return list_data_set

        list_data_set = list()
        for k, v in d.items():
            list_data_set += self.__get_all_dynamic_data_set(v)

        return list_data_set

    def get_binaries_for_dynamic_memory(self) -> bytearray():

        list_data_set = self.__get_all_dynamic_data_set(self.data_on_file)

        data = bytearray()
        list_data_set = list(filter(None, list_data_set))

        data = len(list_data_set).to_bytes(length=1, byteorder="little", signed=False)

        for data_set in list_data_set:
            data += bytearray(data_set.to_bytes())

        return data
