import ctypes
import os
import wave

import tkinter.filedialog
import tkinter.messagebox


class Bos1921DataConverter:
    PCM16_TO_REFERENCE_VALUE = 18799
    MILLI_VOLT_TO_REFERENCE_VALUE = 18.34229

    def __init__(self, wave_file_path: wave, stabilization_value=0,
                 stabilization_duration_ms=5):

        # validate if the wave file path exist and throw an exception if the path is invalid
        if wave_file_path is None:
            raise Exception("The wave file path is null")

        # does the path exist?
        if not os.path.exists(wave_file_path):
            raise Exception("The wave file path does not exist")

        self.wave = wave_file_path
        self.stabilization_value = stabilization_value
        self.stabilization_duration_ms = stabilization_duration_ms

    def convert_to_bytes(self) -> bytearray:

        # open the wave file
        with wave.open(self.wave, "rb") as wave_file:
            # read the wave file
            wave_bytes = wave_file.readframes(wave_file.getnframes())

            # multiple each sample by Bos1921DataConverter.PCM16_TO_REFERENCE_VALUE
            wave_bytes = bytearray(wave_bytes)
            sample_bytes = bytearray()
            for i in range(0, len(wave_bytes), 2):
                sample = int.from_bytes(wave_bytes[i:i + 2], byteorder="little", signed=True)
                sample = (sample * 1000) / Bos1921DataConverter.PCM16_TO_REFERENCE_VALUE

                # rounding to the nearest integer
                sample = round(sample)
                sample = int(sample)

                sample = 0xFFF & sample
                sample = sample.to_bytes(2, byteorder="little", signed=False)

                # append the sample to the sample bytes
                sample_bytes += sample

            # return the bytes
            return sample_bytes


def apply_volume_and_factor_to_reference_data(_data_bytes, volume) -> int:
    for i in range(0, len(_data_bytes), 2):
        _sample = int.from_bytes(_data_bytes[i:i + 2], byteorder="little", signed=True)

        if _sample >= 0x800:
            _sample = ctypes.c_int16(_sample | 0xF000).value

        _sample = (_sample * volume * 1000) / (100 * 1000)
        _sample = int(_sample)

        _sample = _sample & 0xFFF

        _sample = _sample.to_bytes(2, byteorder="little", signed=True)
        _data_bytes[i:i + 2] = _sample

    return int(len(_data_bytes) / 2)


def convert_to_c_array_string(_data_bytes, byteorder="little") -> str:
    samples = list()
    # convert byte endianness from little to big where word size is 2 bytes
    for i in range(0, len(_data_bytes), 2):
        _sample = int.from_bytes(_data_bytes[i:i + 2], byteorder=byteorder)
        _sample = _sample.to_bytes(2, byteorder="big")
        samples[i:i + 2] = _sample

    # convert the bytes into a hex string
    data_string = "0x" + ", 0x".join("{:02x}".format(b) for b in samples)

    # return the string
    return data_string


def add_energy_management_for_press(_data_bytes: bytearray):
    vector = [0, -1, -3, -4, -7]

    for i in range(0, len(vector)):
        vector[i] &= 0x0FFF

    # add to the front of the byte array
    for i in range(-1 * len(vector), 0):
        _data_bytes[0:0] = bytearray(vector[i].to_bytes(2, byteorder="little", signed=False))

    return len(vector)


def add_stabilization(_data_bytes, stabilization_value_volt, stabilization_duration_ms, sampling_rate) -> int:
    # add release stabilization
    referenced_stab_value = int(stabilization_value_volt * Bos1921DataConverter.MILLI_VOLT_TO_REFERENCE_VALUE)

    nbr_samples = int((stabilization_duration_ms / 1000) * sampling_rate)
    referenced_stab_value &= 0xFFF
    stabilization_in_byte_array = referenced_stab_value.to_bytes(2, byteorder="little", signed=False)

    for i in range(0, nbr_samples):
        _data_bytes += stabilization_in_byte_array

    return nbr_samples


if __name__ == "__main__":
    # prompt user for wave file path in a windows dialog
    root = tkinter.Tk()
    root.withdraw()
    root.directory = tkinter.filedialog.askopenfilename(initialdir="/", title="Select file",
                                                        filetypes=(("wave files", "*.wav"), ("all files", "*.*")))

    # create a new instance of the data converter
    data_converter = Bos1921DataConverter(root.directory)
    data_bytes = data_converter.convert_to_bytes()

    waveform_nbr_sample = apply_volume_and_factor_to_reference_data(data_bytes, 66)
    stab_nbr_sample = add_stabilization(data_bytes, -0.150, 3, 8000)
    data_bytes += bytearray(0x0000.to_bytes(2, byteorder="little", signed=False))
    energy_management_nbr_sample = add_energy_management_for_press(data_bytes)

    print("waveform start index : %d stab index : %d Total Length %d", energy_management_nbr_sample,
          waveform_nbr_sample + energy_management_nbr_sample,
          waveform_nbr_sample + energy_management_nbr_sample + stab_nbr_sample)

    print(convert_to_c_array_string(data_bytes))

    # plot the data converted by the data converter
    import matplotlib.pyplot as plt

    samples = list()

    # convert the data sample to 2 bytes integers
    for i in range(0, len(data_bytes), 2):
        sample = int.from_bytes(data_bytes[i:i + 2], byteorder="little")
        if sample >= 0x800:
            sample = ctypes.c_int16(sample | 0xF000).value
        samples.append(sample)

    plt.plot(samples)
    plt.show()
