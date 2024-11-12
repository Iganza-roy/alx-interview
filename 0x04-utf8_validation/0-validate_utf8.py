#!/usr/bin/python3

"""
UTF-8 validation
"""

def validUTF8(data):
    """
    Validates UTF-8 data.
    Args:
        data: List of integers representing UTF-8 data.
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """

    # Ensurin each the data is within the range
    for byte in data:
        if byte < 0 or byte > 255:
            return False
    # Convert data to bytes if not already in the form of integers
    bytes = [int.from_bytes(data[i:i+1],
                            byteorder='big')for i in range(0, len(data), 1)]
    count = 0

    for byte in bytes:
        if count == 0:
            if (byte >> 5) == 0b110:
                count = 1
            elif (byte >> 4) == 0b1110:
                count = 2
            elif (byte >> 3) == 0b11110:
                count = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            count -= 1

    return count == 0