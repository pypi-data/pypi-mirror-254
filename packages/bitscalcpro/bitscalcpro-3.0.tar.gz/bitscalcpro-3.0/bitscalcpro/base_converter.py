#!/usr/bin/env python3
# bitscalcpro/base_converter.py

from bitscalcpro.validator import Validator

class BaseConverter:
    """
    A class for base conversion operations.

    Methods:
    - reverse_order_hex(hex_string): Reverse the order of hexadecimal string.
    - base_converter(input_str, base): Convert input string to hex, octal, and binary based on the specified base.
    - decimal_to_bin_hex_oct(input_dec): Convert decimal input to hex, octal, and binary.
    - hex_to_oct_bin(input_hex): Convert hexadecimal input to octal and binary.
    - oct_to_hex_bin(input_oct): Convert octal input to hex and binary.
    - bin_to_hex_oct(input_dec): Convert binary input to hex and octal.
    """

    @staticmethod
    def reverse_order_hex(hex_string):
        """
        Reverse the order of the hexadecimal string.

        Parameters:
        - hex_string (str): Input hexadecimal string.

        Returns:
        Tuple of reversed 16-bit, 32-bit, 64-bit.
        """
        def reverse_and_chunk(input_string, chunk_size):
            if len(input_string) % chunk_size == 0:
                reversed_chunks = [input_string[i:i + chunk_size] for i in range(0, len(input_string), chunk_size)]
                reversed_chunks = ''.join(reversed(reversed_chunks))
                return ''.join(reversed([reversed_chunks[i:i + 2] for i in range(0, len(reversed_chunks), 2)]))
            else:
                return None

        rev_16bit = reverse_and_chunk(hex_string, 4)
        rev_32bit = reverse_and_chunk(hex_string, 8)
        rev_64bit = reverse_and_chunk(hex_string, 16)

        return rev_16bit, rev_32bit, rev_64bit

    @staticmethod
    def base_converter(input_str, base):
        """
        Convert input string to hex, octal, and binary based on the specified base.

        Parameters:
        - input_str (str): Input string.
        - base (int): Base for conversion.

        Returns:
        Tuple of hex, octal, and binary values.
        """
        try:
            unpacked_int = int(input_str, base)
        except ValueError:
            print("\033[91mInvalid decimal value. Please enter a valid decimal value.\033[0m")
            return None, None, None, None
        hex_value = hex(unpacked_int)[2:]
        oct_value = oct(unpacked_int)[2:]
        bin_value = bin(unpacked_int)[2:]
        return hex_value, oct_value, bin_value

    @staticmethod
    def decimal_to_bin_hex_oct(input_dec):
        """
        Convert decimal input to hex, octal, and binary.

        Parameters:
        - input_dec (str): Decimal input.

        Returns:
        Tuple of hex, octal, and binary values.
        """
        hex_value, oct_value, bin_value = BaseConverter.base_converter(input_dec, 10)
        return hex_value, oct_value, bin_value

    @staticmethod
    def hex_to_oct_bin(input_hex):
        """
        Convert hexadecimal input to octal and binary.

        Parameters:
        - input_hex (str): Hexadecimal input.

        Returns:
        Tuple of octal and binary values.
        """
        _, oct_value, bin_value = BaseConverter.base_converter(input_hex, 16)
        return oct_value, bin_value

    @staticmethod
    def oct_to_hex_bin(input_oct):
        """
        Convert octal input to hex and binary.

        Parameters:
        - input_oct (str): Octal input.

        Returns:
        Tuple of hex and binary values.
        """
        hex_value, _, bin_value = BaseConverter.base_converter(input_oct, 8)
        return hex_value, bin_value

    @staticmethod
    def bin_to_hex_oct(input_dec):
        """
        Convert binary input to hex and octal.

        Parameters:
        - input_dec (str): Binary input.

        Returns:
        Tuple of hex and octal values.
        """
        hex_value, oct_value, _ = BaseConverter.base_converter(input_dec, 2)
        return hex_value, oct_value