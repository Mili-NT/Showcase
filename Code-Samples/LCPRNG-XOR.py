"""
Python Version: 3.6.0
Written For: G4Edit (https://github.com/Mili-NT/g4edit)
Purpose: XOR Pad encryption and decryption via a Linear Congruential Pseudorandom Number Generator. In G4Edit, this
is used to decrypt and encrypt the 236 byte array containing data about the pokemon. This is a heavily modified version
that accepts arbitrary data.

#
# Process Overview:
#
The encryption is done via an XOR Pad using a Linear Congruential Pseudorandom Number Generator, which can be
represented by this function: X[n+1] = (0x41C64E6D * X[n] + 0x6073)

Where x[n] is the seed, and the output x[n+1] is the seed for the next usage of the generator. The first use of the
generator is seeded by the checksum.

By taking the upper 16 bits of the output of the PRNG, we get the values we need to XOR by.
"""
#
# Dependencies
#
import struct
def byte_conversion(data, flag, encode=False):
    """
    This function serves as a wrapper around struct.pack and struct.unpack.
    This is used to encode integers into bytes or decode bytes into integers.

    Note:
    -------------------------------------------------------------------------------------------------------------------
    This dependency is also pulled from G4Edit where this function saw enough use to justify using it as a wrapper.
    -------------------------------------------------------------------------------------------------------------------

    :param data: The data to encode/decode
    :param flag: The struct flag to use for packing/unpacking
    :param encode: True if encoding int->bytes, False if decoding bytes->int
    :return: the packed/unpacked data
    """
    if encode is False:
        return struct.unpack(flag, data)
    else:
        return bytearray(struct.pack(flag, data))
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
    :return: a two-byte bytearray representing the checksum
    """
    data = bytearray([x for x in data])
    high_order, low_order = 0xFF, 0xFF
    for i in range(0, len(data)):
        current_byte = data[i] ^ high_order
        current_byte ^= (current_byte >> 4)
        high_order = (low_order ^ (current_byte >> 3) ^ (current_byte << 4)) & 255
        low_order = (current_byte ^ (current_byte << 5)) & 255
    full_checksum = byte_conversion(high_order << 8 | low_order, 'H', encode=True)
    return full_checksum
#
# Code Sample:
#
def rand(data : bytearray, i : int, seed : int):
    """
    :param data: the entire bytearray being operated on
    :param i: the index of the byte being operated on
    :param seed: If the first usage of the generator, this is the checksum. Else, the output of the previous usage
    :return: The new seed to be used next time the generator is called
    """
    # Implement the function with the passed seed
    seed = ((0xFFFFFFFF & (0x41C64E6D * seed)) + 0x00006073) & 0xFFFFFFFF
    # We need the "upper 16 bits" of the above function, so we shift the seed 16 bits to the right,
    # then convert that to a 2-byte LITTLE-ENDIAN short. The return value is a tuple of (8 bits, 8 bits)
    bits = byte_conversion(seed >> 16, '<H', True)
    # Now we need to "apply the transformation: unencryptedByte = Y xor rand()" where rand() is our upper 16 bits
    # XOR byte at i by first 8 bits of upper 16 bits
    data[i] ^= bits[0]
    # XOR byte at i+1 by second 8 bits of upper 16 bits
    data[i + 1] ^= bits[1]
    # return seed for future generator calls
    return seed
def xor(data : bytearray, seed : int):
    """
    :param data: the entire bytearray being operated on
    :param seed: The seed to pass to rand() calls. This is initially the checksum
    :return: None, modifications are made in place
    """
    # The current seed is set to the passed value (checksum)
    currentseed = seed
    # We iterate over the values between our start and end integer, with a step of 2.
    # The step is because the transformation applied by rand() is "for each 2-byte word Y from 0x08 to 0x87"
    for i in range(0x00, len(data)-2, 2):
        # Call rand() twice to perform the decryption
        rand(data, i, currentseed)
        rand(data, i, currentseed)
        # Call rand a third time to update the currentseed to the output of the PRNG
        currentseed = rand(data, i, currentseed)

def encrypt(data : str):
    """
    :param data: The string to encrypt
    :return: The encrypted bytearray
    """
    data = bytearray(data.encode())
    checksum = calculate_crc_checksum(data)
    initial_seed = byte_conversion(checksum, 'H')[0]
    xor(data, initial_seed)
    data.extend(checksum)
    return data
def decrypt(encrypted_data : bytearray):
    """
    :param encrypted_data: The bytearray returned from encrypt()
    :return: The decrypted string
    """
    decryption_seed = byte_conversion(encrypted_data[-2:], 'H')[0]
    bytes_to_decrypt = encrypted_data[:-2]
    xor(bytes_to_decrypt, decryption_seed)
    return bytes_to_decrypt.decode()

encrypted = encrypt("Linear Congruential Pseudorandom Number Generator")
print(f"Encrypted: {encrypted}")
decrypted = decrypt(encrypted)
print(f"Decrypted: {decrypted}")




