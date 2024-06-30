#!/usr/bin/python3
"""
Module 0-validate_utf8
"""


def validUTF8(data):
    """Check if data is a valid UTF-8 encoding."""
    # keeps track of how many bytes are left to check in
    # a multi-byte UTF-8 character.
    num_bytes = 0

    for num in data:
        # 0xFF is a hexadecimal number that represents 11111111 in binary
        # Ensure we're dealing with only the least significant 8 bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                # pattern indicates the start of a 2-byte character.
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                # pattern indicates the start of a 3-byte character.
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                # pattern indicates the start of a 4-byte character.
                num_bytes = 3
            elif (byte >> 7) == 0b1:
                # Checks if the most significant bit is 1 (i.e., 1xxxxxxx).
                # means it doesn't match any valid UTF-8 start pattern
                return False
        else:
            # For continuation bytes, they must start with '10xxxxxx'
            # If it's part of a multi-byte sequence
            if (byte >> 6) != 0b10:
                return False

            num_bytes -= 1  # Decrease the number of bytes remaining

    # All characters should be fully processed
    return num_bytes == 0
