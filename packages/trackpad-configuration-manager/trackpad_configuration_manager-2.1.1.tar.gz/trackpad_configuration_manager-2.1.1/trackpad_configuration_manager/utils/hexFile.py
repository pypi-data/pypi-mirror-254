import os

from intelhex import IntelHex


class HexFile:
    def __init__(self, data: bytearray, address_offset: int, name, align_length=4):
        file_name = "tmp-bin"

        padding_length = align_length - len(data) % align_length

        if padding_length > 0:
            data += bytearray(0x0 for _ in range(padding_length))

        file_binary = open(file_name, "wb")
        file_binary.write(data)
        file_binary.close()
        self.hFile = IntelHex()
        self.hFile.loadbin(file_name, address_offset)
        self.name = name

        os.remove(file_name)

    def generate_file(self, file_path: str):
        # create the file if it doesn't exist
        open(file_path, 'a').close()
        self.hFile.tofile(file_path, format='hex')
