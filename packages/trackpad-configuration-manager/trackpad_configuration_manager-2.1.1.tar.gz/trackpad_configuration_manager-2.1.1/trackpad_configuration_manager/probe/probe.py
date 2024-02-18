import re

from pyocd.core.helpers import ConnectHelper
from pyocd.flash.file_programmer import FileProgrammer
import time

from trackpad_configuration_manager.cmsis_package import CMSISPackage


class Probe:
    OPS_DELAY_SEC = 0.1
    WORD_LENGTH = 4
    MAX_WORD_PER_READ = 64000

    def __init__(self, unique_id: str, target_id: str, blocking=True, delay_between_ops=False):

        CMSISPackage.load_package()

        self.delay_between_ops = delay_between_ops
        self.unique_id = unique_id
        self.session = ConnectHelper.session_with_chosen_probe(unique_id=unique_id, target_override=target_id,
                                                               blocking=blocking,
                                                               options={"connect_mode": "under-reset",
                                                                        "reset_type": "hw",
                                                                        "hide_programming_progress": True})

        if not self.session:
            raise Exception("Session cannot be established with " + unique_id)

        self.target = self.session.board.target

    def __del__(self):
        self.session.close()

    @staticmethod
    def __nbr_words_for(byte_length: int) -> int:
        length = int(byte_length / Probe.WORD_LENGTH)
        if byte_length % Probe.WORD_LENGTH:
            length += 1
        return length

    @staticmethod
    def __convert_to_byte_array(data_list: list) -> bytearray:
        data = bytearray()
        for word in data_list:
            data += bytearray(word.to_bytes(length=4, byteorder="little", signed=False))

        return data

    @staticmethod
    def scan_for_regex(data_string: str, regex: str) -> str:
        version = str()

        matches = re.finditer(regex, data_string, re.MULTILINE)

        for matchNum, match in enumerate(matches):
            version = match.group()

        return version

    def __read_memory_as_ascii_data(self, address: int, word_length: int) -> str:

        data_list = self.target.read_memory_block32(address, word_length)

        data = self.__convert_to_byte_array(data_list)
        return data.decode('ascii', errors="ignore")

    FULL_VERSION_REGEX = r"\d+\.\d+\.\d+-*\w*\+\d+.\b[0-9a-f]{5,40}\b-*\w*"

    def scan_for_version(self) -> str:

        try:
            self.session.open()
            self.target.halt()

            if self.delay_between_ops is True:
                time.sleep(Probe.OPS_DELAY_SEC)

            flash = self.target.memory_map.get_boot_memory()
            length = self.__nbr_words_for(flash.end - flash.start)

            nbr_words_per_scan = Probe.MAX_WORD_PER_READ if length >= Probe.MAX_WORD_PER_READ else length

            nbr_iteration = int(length / nbr_words_per_scan)

            version = str()

            for i in range(nbr_iteration):
                data = self.__read_memory_as_ascii_data(flash.start + i * nbr_words_per_scan,
                                                        nbr_words_per_scan)

                # detect the string version using regex where the format is x.y.z-TAG+w.hash
                version = self.scan_for_regex(data, self.FULL_VERSION_REGEX)

                if len(version):
                    break
        finally:
            self.target.reset_and_halt()
            self.target.resume()
            self.session.close()

        return version

    def write_data_from_file(self, file_name: str, address: int):

        try:
            self.session.open()
            self.target.halt()

            if self.delay_between_ops is True:
                time.sleep(Probe.OPS_DELAY_SEC)

            programmer = FileProgrammer(self.session)
            programmer.program(file_name, "bin", base_address=address)

        finally:
            self.target.reset_and_halt()
            self.target.resume()
            self.session.close()

    def read_data(self, address: int, length: int) -> bytearray:

        try:
            self.session.open()
            self.target.halt()

            word_length = 4
            length_to_read = int(length / word_length)
            if length % word_length:
                length_to_read += 1

            if self.delay_between_ops is True:
                time.sleep(Probe.OPS_DELAY_SEC)

            data_list = self.target.read_memory_block32(address, length_to_read)
        finally:
            self.target.reset_and_halt()
            self.target.resume()
            self.session.close()

        return self.__convert_to_byte_array(data_list)
