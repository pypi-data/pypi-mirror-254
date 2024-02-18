import crc


def compute_crc(data: bytearray) -> int:
    width = 16
    poly = 0x1189
    init_value = 0xFFFF
    final_xor_value = 0x00
    reverse_input = False
    reverse_output = False

    configuration = crc.Configuration(width, poly, init_value, final_xor_value, reverse_input, reverse_output)
    use_table = True
    crc_calculator = crc.CrcCalculator(configuration, use_table)

    return crc_calculator.calculate_checksum(data)
