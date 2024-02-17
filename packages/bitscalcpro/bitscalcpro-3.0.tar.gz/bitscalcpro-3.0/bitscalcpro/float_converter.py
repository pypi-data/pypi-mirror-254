#!/usr/bin/env python3
# bitscalcpro/float_converter.py

import struct

class FloatConverter:
    """
    A class for floating-point number conversion operations.

    Methods:
    - base_to_float(input_value, base): Convert base-based input to a floating-point number.
    - base_to_double(input_value, base): Convert base-based input to a double-precision floating-point number.
    - hex_to_float(input_hex): Convert hexadecimal input to a floating-point number.
    - hex_to_double(input_hex): Convert hexadecimal input to a double-precision floating-point number.
    - oct_to_float(input_oct): Convert octal input to a floating-point number.
    - oct_to_double(input_oct): Convert octal input to a double-precision floating-point number.
    - bin_to_float(input_bin): Convert binary input to a floating-point number.
    - bin_to_double(input_bin): Convert binary input to a double-precision floating-point number.
    - float_double_to_oct_bin_hex(input_value, format_char, max_value): Convert float or double input to octal, binary, and hexadecimal.
    - float_to_oct_bin_hex(input_float): Convert float input to octal, binary, and hexadecimal.
    - double_to_oct_bin_hex(input_double): Convert double input to octal, binary, and hexadecimal.
    """

    @staticmethod
    def base_to_float(input_value, base):
        """
        Convert base-based input to a floating-point number.

        Parameters:
        - input_value (str): Input value in the specified base.
        - base (int): Base for conversion.

        Returns:
        Floating-point number.
        """
        try:
            unpacked_int = int(input_value, base)
            return struct.unpack('>f', struct.pack('>I', unpacked_int))[0]
        except ValueError:
            print(f"\033[91mInvalid {base}-based value. Please enter a valid {base}-based value.\033[0m")
        except struct.error:
            pass

    @staticmethod
    def base_to_double(input_value, base):
        """
        Convert base-based input to a double-precision floating-point number.

        Parameters:
        - input_value (str): Input value in the specified base.
        - base (int): Base for conversion.

        Returns:
        Double-precision floating-point number.
        """
        try:
            unpacked_int = int(input_value, base)
            return struct.unpack('>d', struct.pack('>Q', unpacked_int))[0]
        except ValueError:
            print(f"\033[91mInvalid {base}-based value. Please enter a valid {base}-based value.\033[0m")
        except struct.error:
            pass

    @staticmethod
    def hex_to_float(input_hex):
        """
        Convert hexadecimal input to a floating-point number.

        Parameters:
        - input_hex (str): Hexadecimal input.

        Returns:
        Floating-point number.
        """
        return FloatConverter.base_to_float(input_hex, 16)

    @staticmethod
    def hex_to_double(input_hex):
        """
        Convert hexadecimal input to a double-precision floating-point number.

        Parameters:
        - input_hex (str): Hexadecimal input.

        Returns:
        Double-precision floating-point number.
        """
        return FloatConverter.base_to_double(input_hex, 16)

    @staticmethod
    def oct_to_float(input_oct):
        """
        Convert octal input to a floating-point number.

        Parameters:
        - input_oct (str): Octal input.

        Returns:
        Floating-point number.
        """
        return FloatConverter.base_to_float(input_oct, 8)

    @staticmethod
    def oct_to_double(input_oct):
        """
        Convert octal input to a double-precision floating-point number.

        Parameters:
        - input_oct (str): Octal input.

        Returns:
        Double-precision floating-point number.
        """
        return FloatConverter.base_to_double(input_oct, 8)

    @staticmethod
    def bin_to_float(input_bin):
        """
        Convert binary input to a floating-point number.

        Parameters:
        - input_bin (str): Binary input.

        Returns:
        Floating-point number.
        """
        return FloatConverter.base_to_float(input_bin, 2)

    @staticmethod
    def bin_to_double(input_bin):
        """
        Convert binary input to a double-precision floating-point number.

        Parameters:
        - input_bin (str): Binary input.

        Returns:
        Double-precision floating-point number.
        """
        return FloatConverter.base_to_double(input_bin, 2)

    @staticmethod
    def float_double_to_oct_bin_hex(input_value, format_char, max_value):
        """
        Convert float or double input to octal, binary, and hexadecimal.

        Parameters:
        - input_value (float or double): Input value.
        - format_char (str): Format character for packing.
        - max_value (float or double): Maximum representable value.

        Returns:
        Tuple of octal, binary, and hexadecimal values.
        """
        try:
            if abs(input_value) > max_value:
                raise OverflowError(f"\033[91mValue exceeds maximum representable value: {max_value}.\033[0m")
            packed_value = struct.pack(format_char, input_value)
            unpacked_int = struct.unpack('>Q' if format_char == '>d' else '>I', packed_value)[0]
            hex_value = hex(unpacked_int)[2:]
            oct_value = oct(unpacked_int)[2:]
            bin_value = bin(unpacked_int)[2:]
            return oct_value, bin_value, hex_value
        except ValueError:
            print(f"\033[91mInvalid value. Please enter a valid value.\033[0m")
        except OverflowError as e:
            print(f"\n\033[91m{e} Please enter a smaller value.\033[0m")
        except struct.error:
            pass

    @staticmethod
    def float_to_oct_bin_hex(input_float):
        """
        Convert float input to octal, binary, and hexadecimal.

        Parameters:
        - input_float (float): Input float value.

        Returns:
        Tuple of octal, binary, and hexadecimal values.
        """
        return FloatConverter.float_double_to_oct_bin_hex(input_float, '>f', 3.4028235e+38)

    @staticmethod
    def double_to_oct_bin_hex(input_double):
        """
        Convert double input to octal, binary, and hexadecimal.

        Parameters:
        - input_double (double): Input double value.

        Returns:
        Tuple of octal, binary, and hexadecimal values.
        """
        return FloatConverter.float_double_to_oct_bin_hex(input_double, '>d', 1.7976931348623157e+308)