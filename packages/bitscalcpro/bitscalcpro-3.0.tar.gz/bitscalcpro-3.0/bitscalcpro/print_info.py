#!/usr/bin/env python3
# bitscalcpro/print_info.py

from bitscalcpro.validator import Validator
from bitscalcpro.float_converter import FloatConverter
from bitscalcpro.base_converter import BaseConverter
from decimal import Decimal

class PrintInfo:
    """
    Class containing methods to print information and results in the bitscalcpro application.

    Methods:
    - print_bits_info(user_input): Prints the bit size information based on the user input.
    - print_result(user_input): Prints the results for different representations based on the user input.
    - print_decimal_info(user_input): Prints decimal-related information and results.
    - print_binary_info(user_input): Prints binary-related information and results.
    - print_octal_info(user_input): Prints octal-related information and results.
    - print_hexadecimal_info_normal(hex_value): Prints normal-order hexadecimal information and results.
    - print_hexadecimal_info_reversed_16bit(hex_value): Prints reversed 16-bit hexadecimal information and results.
    - print_hexadecimal_info_reversed_32bit(hex_value): Prints reversed 32-bit hexadecimal information and results.
    - print_hexadecimal_info_reversed_64bit(hex_value): Prints reversed 64-bit hexadecimal information and results.
    - print_float_info(user_input): Prints float-related information and results.
    - print_double_info(user_input): Prints double-related information and results.
    """
    
    @staticmethod
    def print_bits_info(user_input):
        """
        Prints the bit size information based on the user input.

        Args:
        - user_input (str): User input value.

        Raises:
        - ValueError: If the input is invalid.
        """
        try:
            decimal_value = 0
            print("\n\033[1;33mSize Info:\033[0m")
            if Validator.is_binary_code(user_input):
                print(f"\033[1;32mSize of Binary:\033[0m \033[1;36m{len(user_input)}-bits\033[0m")
            if Validator.is_octal_code(user_input):
                octal_value = int(user_input, 8)
                print(f"\033[1;32mBits size of Octal:\033[0m \033[1;36m{octal_value.bit_length()}-bits\033[0m")
            if Validator.is_decimal_code(user_input):
                octal_value = int(user_input, 10)
                print(f"\033[1;32mBits size of Decimal:\033[0m \033[1;36m{octal_value.bit_length()}-bits\033[0m")
            if Validator.is_hex_code(user_input):
                hex_value = int(user_input, 16)
                print(f"\033[1;32mBits size of Hexadecimal:\033[0m \033[1;36m{hex_value.bit_length()}-bits\033[0m")
            if Validator.is_float_code(user_input):
                float_value = float(user_input)
                _, bin_value, _ = FloatConverter.float_to_oct_bin_hex(float_value)
                print(f"\033[1;32mBits size of Float:\033[0m \033[1;36m{len(bin_value)}-bits\033[0m")
            if Validator.is_double_code(user_input):
                float_value = float(user_input)
                _, bin_value, _ = FloatConverter.double_to_oct_bin_hex(float_value)
                print(f"\033[1;32mBits size of Double:\033[0m \033[1;36m{len(bin_value)}-bits\033[0m")
        except ValueError:
            print("\033[91mInvalid input. Please enter a valid float, hex, octal, or binary value.\033[0m")

    @staticmethod
    def print_bits_info2(user_input, suffix):
        """
        Prints the bit size information based on the user input and suffix.
    
        Args:
            user_input (str): User input value.
            suffix (str): Suffix indicating the type of representation.
    
        Raises:
            ValueError: If the input is invalid.
        """
        try:
            decimal_value = 0
            print("\n\033[1;33mSize Info:\033[0m")
            if Validator.is_binary_code(user_input) and suffix == 'binary':
                print(f"\033[1;32mSize of Binary:\033[0m \033[1;36m{len(user_input)}-bits\033[0m")
            elif Validator.is_octal_code(user_input) and suffix == 'octal':
                octal_value = int(user_input, 8)
                print(f"\033[1;32mBits size of Octal:\033[0m \033[1;36m{octal_value.bit_length()}-bits\033[0m")
            elif Validator.is_decimal_code(user_input) and suffix == 'decimal':
                octal_value = int(user_input, 10)
                print(f"\033[1;32mBits size of Decimal:\033[0m \033[1;36m{octal_value.bit_length()}-bits\033[0m")
            elif Validator.is_hex_code(user_input) and suffix == 'hexadecimal':
                hex_value = int(user_input, 16)
                print(f"\033[1;32mBits size of Hexadecimal:\033[0m \033[1;36m{hex_value.bit_length()}-bits\033[0m")
            elif Validator.is_float_code(user_input) and suffix == 'float':
                float_value = float(user_input)
                _, bin_value, _ = FloatConverter.float_to_oct_bin_hex(float_value)
                print(f"\033[1;32mBits size of Float:\033[0m \033[1;36m{len(bin_value)}-bits\033[0m")
            elif Validator.is_double_code(user_input) and suffix == 'double':
                float_value = float(user_input)
                _, bin_value, _ = FloatConverter.double_to_oct_bin_hex(float_value)
                print(f"\033[1;32mBits size of Double:\033[0m \033[1;36m{len(bin_value)}-bits\033[0m")
            else:
                print("\033[91mInvalid input. Please enter a valid float, hex, octal, or binary value with valid suffix.\033[0m")
        except ValueError:
            print("\033[91mInvalid input. Please enter a valid float, hex, octal, or binary value.\033[0m")
    
    @staticmethod
    def print_result(user_input):
        """
        Prints the results for different representations based on the user input.

        Args:
        - user_input (str): User input value.

        Raises:
        - ValueError: If the input is invalid.
        - OverflowError: If the value exceeds the maximum representable value.
        """
        try:
            if Validator.is_decimal_code(user_input):
                print("\n\033[1;33mDecimal Results:\033[0m")
                PrintInfo.print_decimal_info(user_input)
            if Validator.is_binary_code(user_input):
                print("\n\033[1;33mBinary Results:\033[0m")
                PrintInfo.print_binary_info(user_input)
            if Validator.is_octal_code(user_input):
                print("\n\033[1;33mOctal Results:\033[0m")
                PrintInfo.print_octal_info(user_input)
            if Validator.is_hex_code(user_input):
                print("\n\033[1;33mHexadecimal Results:\033[0m")
                PrintInfo.print_hexadecimal_info_normal(user_input)
                hex_value = user_input.lower()
                if len(hex_value) % 4 == 0:
                    PrintInfo.print_hexadecimal_info_reversed_16bit(user_input)
                if len(hex_value) % 8 == 0:
                    PrintInfo.print_hexadecimal_info_reversed_32bit(user_input)
                if len(hex_value) % 16 == 0:
                    PrintInfo.print_hexadecimal_info_reversed_64bit(user_input)
            if Validator.is_float_code(user_input):
                print("\n\033[1;33mFloat Results:\033[0m")
                PrintInfo.print_float_info(user_input)
            if Validator.is_double_code(user_input):
                print("\n\033[1;33mDouble Results:\033[0m")
                PrintInfo.print_double_info(user_input)
        except ValueError:
            print("\033[91mInvalid input. Please enter a valid float, decimal hex, octal, or binary value.\033[0m")
        except OverflowError as e:
            print(f"\n\033[91m{e} Please enter a smaller value.\033[0m")
    
    @staticmethod
    def print_result2(user_input, suffix):
        """
        Prints the results for different representations based on the user input and suffix.
    
        Args:
            user_input (str): User input value.
            suffix (str): Suffix indicating the type of representation.
    
        Raises:
            ValueError: If the input is invalid.
            OverflowError: If the value exceeds the maximum representable value.
        """
        try:
            if Validator.is_decimal_code(user_input) and suffix == 'decimal':
                print("\n\033[1;33mDecimal Results:\033[0m")
                PrintInfo.print_decimal_info(user_input)
            elif Validator.is_binary_code(user_input) and suffix == 'binary':
                print("\n\033[1;33mBinary Results:\033[0m")
                PrintInfo.print_binary_info(user_input)
            elif Validator.is_octal_code(user_input) and suffix == 'octal':
                print("\n\033[1;33mOctal Results:\033[0m")
                PrintInfo.print_octal_info(user_input)
            elif Validator.is_hex_code(user_input) and suffix == 'hexadecimal':
                print("\n\033[1;33mHexadecimal Results:\033[0m")
                PrintInfo.print_hexadecimal_info_normal(user_input)
                hex_value = user_input.lower()
                if len(hex_value) % 4 == 0:
                    PrintInfo.print_hexadecimal_info_reversed_16bit(user_input)
                if len(hex_value) % 8 == 0:
                    PrintInfo.print_hexadecimal_info_reversed_32bit(user_input)
                if len(hex_value) % 16 == 0:
                    PrintInfo.print_hexadecimal_info_reversed_64bit(user_input)
            elif Validator.is_float_code(user_input) and suffix == 'float':
                print("\n\033[1;33mFloat Results:\033[0m")
                PrintInfo.print_float_info(user_input)
            elif Validator.is_double_code(user_input) and suffix == 'double':
                print("\n\033[1;33mDouble Results:\033[0m")
                PrintInfo.print_double_info(user_input)
            else:
                print("\033[91mInvalid input. Please enter a valid float, decimal hex, octal, or binary value with valid suffix.\033[0m")
        except ValueError:
            print("\033[91mInvalid input. Please enter a valid float, decimal hex, octal, or binary value.\033[0m")
        except OverflowError as e:
            print(f"\n\033[91m{e} Please enter a smaller value.\033[0m")
            
    @staticmethod
    def print_decimal_info(user_input):
        """
        Prints decimal-related information and results.

        Args:
        - user_input (str): User input value.
        """
        hex_value, oct_result, bin_result = BaseConverter.decimal_to_bin_hex_oct(user_input)
        print(f"\033[1;32mDecimal to Hexadecimal (Normal Order):\033[0m \033[1;36m{hex_value}\033[0m")
        rev_16bit, rev_32bit, rev_64bit = BaseConverter.reverse_order_hex(hex_value)
        if rev_16bit is not None:
            print(f"\033[1;32mDecimal to Hexadecimal (Reversed 16-bit):\033[0m \033[1;36m{rev_16bit}\033[0m")
        if rev_32bit is not None:
            print(f"\033[1;32mDecimal to Hexadecimal (Reversed 32-bit):\033[0m \033[1;36m{rev_32bit}\033[0m")
        if rev_64bit is not None:
            print(f"\033[1;32mDecimal to Hexadecimal (Reversed 64-bit):\033[0m \033[1;36m{rev_64bit}\033[0m")
        print(f"\033[1;32mDecimal to Octal:\033[0m \033[1;36m{oct_result}\033[0m")
        print(f"\033[1;32mDecimal to Binary:\033[0m \033[1;36m{bin_result}\033[0m")
            
    @staticmethod
    def print_binary_info(user_input):
        """
        Prints binary-related information and results.

        Args:
        - user_input (str): User input value.
        """
        decimal_value = int(user_input, 2)
        print(f"\033[1;32mBinary to Decimal:\033[0m \033[1;36m{decimal_value}\033[0m")
        hex_value, oct_result = BaseConverter.bin_to_hex_oct(user_input)
        print(f"\033[1;32mBinary to Hexadecimal (Normal Order):\033[0m \033[1;36m{hex_value}\033[0m")
        rev_16bit, rev_32bit, rev_64bit = BaseConverter.reverse_order_hex(hex_value)
        if rev_16bit is not None:
            print(f"\033[1;32mBinary to Hexadecimal (Reversed 16-bit):\033[0m \033[1;36m{rev_16bit}\033[0m")
        if rev_32bit is not None:
            print(f"\033[1;32mBinary to Hexadecimal (Reversed 32-bit):\033[0m \033[1;36m{rev_32bit}\033[0m")
        if rev_64bit is not None: 
            print(f"\033[1;32mBinary to Hexadecimal (Reversed 64-bit):\033[0m \033[1;36m{rev_64bit}\033[0m")
        print(f"\033[1;32mBinary to Octal:\033[0m \033[1;36m{oct_result}\033[0m")
        float_result = FloatConverter.bin_to_float(user_input)
        print(f"\033[1;32mBinary to Float:\033[0m \033[1;36m{float_result}\033[0m")
        double_result = FloatConverter.bin_to_double(user_input)
        print(f"\033[1;32mBinary to Double:\033[0m \033[1;36m{double_result}\033[0m")
    
    @staticmethod
    def print_octal_info(user_input):
        """
        Prints octal-related information and results.

        Args:
        - user_input (str): User input value.
        """
        decimal_value = int(user_input, 8)
        print(f"\033[1;32mOctal to Decimal:\033[0m \033[1;36m{decimal_value}\033[0m")
        hex_value, bin_result = BaseConverter.oct_to_hex_bin(user_input)
        print(f"\033[1;32mOctal to Hexadecimal (Normal Order):\033[0m \033[1;36m{hex_value}\033[0m")
        rev_16bit, rev_32bit, rev_64bit = BaseConverter.reverse_order_hex(hex_value)
        if rev_16bit is not None:
            print(f"\033[1;32mOctal to Hexadecimal (Reversed 16-bit):\033[0m \033[1;36m{rev_16bit}\033[0m")
        if rev_32bit is not None:
            print(f"\033[1;32mOctal to Hexadecimal (Reversed 32-bit):\033[0m \033[1;36m{rev_32bit}\033[0m")
        if rev_64bit is not None:
            print(f"\033[1;32mOctal to Hexadecimal (Reversed 64-bit):\033[0m \033[1;36m{rev_64bit}\033[0m")
        print(f"\033[1;32mOctal to Binary:\033[0m \033[1;36m{bin_result}\033[0m")
        float_result = FloatConverter.oct_to_float(user_input)
        print(f"\033[1;32mOctal to Float:\033[0m \033[1;36m{float_result}\033[0m")
        double_result = FloatConverter.oct_to_double(user_input)
        print(f"\033[1;32mOctal to Double:\033[0m \033[1;36m{double_result}\033[0m")    

    @staticmethod
    def print_hexadecimal_info_normal(hex_value):
        """
        Prints normal mode hexadecimal information and results.

        Args:
        - hex_value (str): Hexadecimal input value.
        """
        print(f"\033[1;35mNormal Mode:\033[0m")
        print(f"\033[1;32mNormal-Order:\033[0m \033[1;36m{hex_value}\033[0m")
        hex_value = str(hex_value)
        decimal_value = int(hex_value, 16)
        print(f"\033[1;32mHexadecimal to Decimal:\033[0m \033[1;36m{decimal_value}\033[0m")
        oct_result, bin_result = BaseConverter.hex_to_oct_bin(hex_value)
        print(f"\033[1;32mHexadecimal to Octal:\033[0m \033[1;36m{oct_result}\033[0m")
        print(f"\033[1;32mHexadecimal to Binary:\033[0m \033[1;36m{bin_result}\033[0m")
        float_result = FloatConverter.hex_to_float(hex_value.lower())
        print(f"\033[1;32mHexadecimal to Float:\033[0m \033[1;36m{float_result}\033[0m")
        double_result = FloatConverter.hex_to_double(hex_value.lower())
        print(f"\033[1;32mHexadecimal to Double:\033[0m \033[1;36m{double_result}\033[0m")
    
    @staticmethod
    def print_hexadecimal_info_reversed_16bit(hex_value):
        """
        Prints reversed mode 01 hexadecimal information and results.

        Args:
        - hex_value (str): Hexadecimal input value.
        """
        print(f"\033[1;35mReversed 16-bit:\033[0m")
        hex_value = str(hex_value)
        rev_16bit, _, _ = BaseConverter.reverse_order_hex(hex_value)
        print(f"\033[1;32mReversed-Order:\033[0m \033[1;36m{rev_16bit}\033[0m")
        decimal_value = int(rev_16bit, 16)
        print(f"\033[1;32mHexadecimal to Decimal:\033[0m \033[1;36m{decimal_value}\033[0m")
        oct_result, bin_result = BaseConverter.hex_to_oct_bin(rev_16bit)
        print(f"\033[1;32mHexadecimal to Octal:\033[0m \033[1;36m{oct_result}\033[0m")
        print(f"\033[1;32mHexadecimal to Binary:\033[0m \033[1;36m{bin_result}\033[0m")
        float_result = FloatConverter.hex_to_float(rev_16bit.lower())
        print(f"\033[1;32mHexadecimal to Float:\033[0m \033[1;36m{float_result}\033[0m")
        double_result = FloatConverter.hex_to_double(rev_16bit.lower())
        print(f"\033[1;32mHexadecimal to Double:\033[0m \033[1;36m{double_result}\033[0m")
        
    @staticmethod
    def print_hexadecimal_info_reversed_32bit(hex_value):
        """
        Prints reversed mode 02 hexadecimal information and results.

        Args:
        - hex_value (str): Hexadecimal input value.
        """
        print(f"\033[1;35mReversed 32-bit:\033[0m")
        hex_value = str(hex_value)
        _, rev_32bit, _ = BaseConverter.reverse_order_hex(hex_value)
        print(f"\033[1;32mReversed-Order:\033[0m \033[1;36m{rev_32bit}\033[0m")
        decimal_value = int(rev_32bit, 16)
        print(f"\033[1;32mHexadecimal to Decimal:\033[0m \033[1;36m{decimal_value}\033[0m")
        oct_result, bin_result = BaseConverter.hex_to_oct_bin(rev_32bit)
        print(f"\033[1;32mHexadecimal to Octal:\033[0m \033[1;36m{oct_result}\033[0m")
        print(f"\033[1;32mHexadecimal to Binary:\033[0m \033[1;36m{bin_result}\033[0m")
        float_result = FloatConverter.hex_to_float(rev_32bit.lower())
        print(f"\033[1;32mHexadecimal to Float:\033[0m \033[1;36m{float_result}\033[0m")
        double_result = FloatConverter.hex_to_double(rev_32bit.lower())
        print(f"\033[1;32mHexadecimal to Double:\033[0m \033[1;36m{double_result}\033[0m")
        
    @staticmethod
    def print_hexadecimal_info_reversed_64bit(hex_value):
        """
        Prints reversed mode 03 hexadecimal information and results.

        Args:
        - hex_value (str): Hexadecimal input value.
        """
        print(f"\033[1;35mReversed 64-bit:\033[0m")
        hex_value = str(hex_value)
        _, _, rev_64bit = BaseConverter.reverse_order_hex(hex_value)
        print(f"\033[1;32mReversed-Order:\033[0m \033[1;36m{rev_64bit}\033[0m")
        decimal_value = int(rev_64bit, 16)
        print(f"\033[1;32mHexadecimal to Decimal:\033[0m \033[1;36m{decimal_value}\033[0m")
        oct_result, bin_result = BaseConverter.hex_to_oct_bin(rev_64bit)
        print(f"\033[1;32mHexadecimal to Octal:\033[0m \033[1;36m{oct_result}\033[0m")
        print(f"\033[1;32mHexadecimal to Binary:\033[0m \033[1;36m{bin_result}\033[0m")
        float_result = FloatConverter.hex_to_float(rev_64bit.lower())
        print(f"\033[1;32mHexadecimal to Float:\033[0m \033[1;36m{float_result}\033[0m")
        double_result = FloatConverter.hex_to_double(rev_64bit.lower())
        print(f"\033[1;32mHexadecimal to Double:\033[0m \033[1;36m{double_result}\033[0m")
        
    @staticmethod
    def print_float_info(user_input):
        """
        Prints float-related information and results.

        Args:
        - user_input (str): User input value.
        """
        float_value = float(user_input)
        if float_value is not None:
            dec_result = Decimal(float_value)
            print(f"\033[1;32mValue actually stored in float:\033[0m \033[1;36m{dec_result}\033[0m")
            result = FloatConverter.float_to_oct_bin_hex(float_value)
            if result is not None:
                oct_result, bin_result, hex_value = result
                rev_16bit, rev_32bit, rev_64bit = BaseConverter.reverse_order_hex(hex_value)
                print(f"\033[1;32mFloat to Hexadecimal (Normal Order):\033[0m \033[1;36m{hex_value}\033[0m")
                print(f"\033[1;32mFloat to Hexadecimal (Reversed 16-bit):\033[0m \033[1;36m{rev_16bit}\033[0m")
                print(f"\033[1;32mFloat to Hexadecimal (Reversed 32-bit):\033[0m \033[1;36m{rev_32bit}\033[0m")
                print(f"\033[1;32mFloat to Hexadecimal (Reversed 64-bit):\033[0m \033[1;36m{rev_64bit}\033[0m")
                print(f"\033[1;32mFloat to Octal:\033[0m \033[1;36m{oct_result}\033[0m")
                print(f"\033[1;32mFloat to Binary:\033[0m \033[1;36m{bin_result}\033[0m")
    
    @staticmethod
    def print_double_info(user_input):
        """
        Prints double-related information and results.

        Args:
        - user_input (str): User input value.
        """
        double_value = float(user_input)
        if double_value is not None:
            dec_result = Decimal(double_value)
            print(f"\033[1;32mValue actually stored in double:\033[0m \033[1;36m{dec_result}\033[0m")
            result = FloatConverter.double_to_oct_bin_hex(double_value)
            if result is not None:
                oct_result, bin_result, hex_value = result
                rev_16bit, rev_32bit, rev_64bit = BaseConverter.reverse_order_hex(hex_value)
                print(f"\033[1;32mDouble to Hexadecimal (Normal Order):\033[0m \033[1;36m{hex_value}\033[0m")
                print(f"\033[1;32mDouble to Hexadecimal (Reversed 16-bit):\033[0m \033[1;36m{rev_16bit}\033[0m")
                print(f"\033[1;32mDouble to Hexadecimal (Reversed 32-bit):\033[0m \033[1;36m{rev_32bit}\033[0m")
                print(f"\033[1;32mDouble to Hexadecimal (Reversed 64-bit):\033[0m \033[1;36m{rev_64bit}\033[0m")
                print(f"\033[1;32mDouble to Octal:\033[0m \033[1;36m{oct_result}\033[0m")
                print(f"\033[1;32mDouble to Binary:\033[0m \033[1;36m{bin_result}\033[0m")