import wave

from trackpad_configuration_manager.boreas_data_converter.bos1921DataConverter import Bos1921DataConverter
from trackpad_configuration_manager.dataHolder import WavefileDataHolder, DynamicDataSet, \
    DynamicSectionNotFoundException, DynamicDataSetType
from trackpad_configuration_manager.utils.crc16 import compute_crc


class Bos1921FeedbackDataSet(DynamicDataSet):

    def __init__(self, data: bytearray, sampling_rate: int):
        self.sampling_rate_khz = int(sampling_rate / 1000)
        super().__init__(data, DynamicDataSetType.BOS1921_REFERENCED_FEEDBACK)

    def to_bytes(self) -> bytes:
        data = bytearray(self.type.value.to_bytes(length=1, byteorder="little", signed=False))  # data type
        data += bytearray(self.sampling_rate_khz.to_bytes(length=4, byteorder="little", signed=False))  # sampling rate
        data += bytearray(len(self.data).to_bytes(length=2, byteorder="little", signed=False))  # data length
        data += bytearray(self.data)  # data

        data += bytearray(compute_crc(data).to_bytes(length=2, byteorder="little", signed=False))  # crc

        return bytes(data)


class Bos1921WavefileDataHolder(WavefileDataHolder):
    def __init__(self, file_value: dict, base_location: str):
        super().__init__(file_value, base_location)
        self.__update_sampling_rate()

    def __update_sampling_rate(self):
        # open wavefile and read the sampling rate from the wavefile header
        self.sampling_rate = wave.open(self.base_location + "\\" + self.on_file.path, "rb").getframerate()

    def update_on_file(self, file_path: str):
        super().update_on_file(file_path)
        self.__update_sampling_rate()

    def get_dynamic_memory_section(self) -> DynamicDataSet:

        try:
            data_converter = Bos1921DataConverter(self.base_location + "\\" + self.on_file.path)
            data = data_converter.convert_to_bytes()
        except Exception:
            raise DynamicSectionNotFoundException(self.base_location + "\\" + self.on_file.path)

        return Bos1921FeedbackDataSet(data, self.sampling_rate)
