"""
Python Version: 3.6.0
Written For: G4Edit (https://github.com/Mili-NT/g4edit)
Purpose: Checksumming via a 17 bit CRC implementation
"""

def calculate_crc_checksum(data):
    """
    The checksum is calculated with a CRC-16-CCITT (17 bit) cyclic redundancy check algorithm.
                    https://en.wikipedia.org/wiki/Cyclic_redundancy_check
    --------------------------------------------------------------------------------------------------
    Here is a basic explanation of how CRCs are computed.
    To compute an n-bit binary CRC, line the bits representing the input in a row,
    and position the (n + 1)-bit pattern representing the CRC's divisor (called a "polynomial")
    underneath the left-hand end of the row... The polynomial is written in binary as the coefficients
    --------------------------------------------------------------------------------------------------

    :param data: the block of data to generate a checksum for
    :return: a two-byte checksum packed into an unsigned short
    """
    data = bytearray([x for x in data])
    high_order, low_order = 0xFF, 0xFF
    for i in range(0, len(data)):
        current_byte = data[i] ^ high_order
        current_byte ^= (current_byte >> 4)
        high_order = (low_order ^ (current_byte >> 3) ^ (current_byte << 4)) & 255
        low_order = (current_byte ^ (current_byte << 5)) & 255
    full_checksum = byte_conversion(high_order << 8 | low_order, 'H', encode=True)[0]
    return full_checksum
