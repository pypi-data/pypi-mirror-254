#!/usr/bin/env python3
# bitscalcpro/validator.py

import sys
import re

class Validator:
    """
    A class providing methods for input validation and code type detection.

    Methods:
    - input_validation(user_input): Validates user input and removes unnecessary characters.
    - is_numeric_code(user_input, base): Checks if the user input is a valid numeric value in the specified base.
    - is_decimal_code(user_input): Checks if the user input is a valid decimal value.
    - is_hex_code(user_input): Checks if the user input is a valid hexadecimal value.
    - is_octal_code(user_input): Checks if the user input is a valid octal value.
    - is_binary_code(user_input): Checks if the user input is a valid binary value.
    - is_float_code(user_input): Checks if the user input is a valid float value.
    - is_double_code(user_input): Checks if the user input is a valid double value.
    """
    
    @staticmethod
    def input_validation(user_input):
        """
        Validates user input and removes unnecessary characters.

        Args:
        - user_input (str): User input value.

        Returns:
        - str: Processed and validated user input.
        """
        valid_chars = set("0123456789abcdef.-+")
        user_input = re.sub(r'(?:^(0x|0o|0b|[-+])|\s)', '', user_input, flags=re.IGNORECASE)
        if not user_input:
            print("\033[1;34m\nProgram terminated.\033[0m")
            sys.exit()
        while not all(char in valid_chars for char in user_input.lower()):
            print("\033[91mInvalid input. Please enter a valid float, decimal hex, octal, or binary value.\033[0m")
            user_decision = input("\033[93mEnter a valid input or press Enter to terminate the program: \033[0m")
            if not user_decision:
                print("\033[1;34m\nProgram terminated.\033[0m")
                sys.exit()
            user_input = re.sub(r'(?:^(0x|0o|0b|[-+])|\s)', '', user_decision, flags=re.IGNORECASE)
        return user_input
    
    @staticmethod
    def is_numeric_code(user_input, base):
        """
        Checks if the user input is a valid numeric value in the specified base.

        Args:
        - user_input (str): User input value.
        - base (int): Numeric base to check validity.

        Returns:
        - bool: True if valid numeric value, False otherwise.
        """
        try:
            int(user_input, base)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_decimal_code(user_input):
        """
        Checks if the user input is a valid decimal value.

        Args:
        - user_input (str): User input value.

        Returns:
        - bool: True if valid decimal value, False otherwise.
        """
        return Validator.is_numeric_code(user_input, 10)

    @staticmethod
    def is_hex_code(user_input):
        """
        Checks if the user input is a valid hexadecimal value.

        Args:
        - user_input (str): User input value.

        Returns:
        - bool: True if valid hexadecimal value, False otherwise.
        """
        return Validator.is_numeric_code(user_input, 16)

    @staticmethod
    def is_octal_code(user_input):
        """
        Checks if the user input is a valid octal value.

        Args:
        - user_input (str): User input value.

        Returns:
        - bool: True if valid octal value, False otherwise.
        """
        return Validator.is_numeric_code(user_input, 8)

    @staticmethod
    def is_binary_code(user_input):
        """
        Checks if the user input is a valid binary value.

        Args:
        - user_input (str): User input value.

        Returns:
        - bool: True if valid binary value, False otherwise.
        """
        return Validator.is_numeric_code(user_input, 2)

    @staticmethod
    def is_float_code(user_input):
        """
        Checks if the user input is a valid float value.

        Args:
        - user_input (str): User input value.

        Returns:
        - bool: True if valid float value, False otherwise.
        """
        try:
            float_value = float(user_input)
            if abs(float_value) > 3.4028235e+38:
                return False
            return True
        except ValueError:
            return False

    @staticmethod
    def is_double_code(user_input):
        """
        Checks if the user input is a valid double value.

        Args:
        - user_input (str): User input value.

        Returns:
        - bool: True if valid double value, False otherwise.
        """
        try:
            double_value = float(user_input)
            if abs(double_value) > 1.7976931348623157e+308:
                return False
            return True
        except ValueError:
            return False

    @staticmethod
    def suffix_representation(user_input):
        """
        Determine the representation type of a given suffix.
    
        Args:
            user_input (str): The input string containing a suffix.
    
        Returns:
            str: The representation type corresponding to the suffix:
                 - 'hexadecimal' for '-x'
                 - 'decimal' for '-d'
                 - 'octal' for '-o'
                 - 'binary' for '-b'
                 - 'float' for '-f'
                 - 'double' for '-dd'
                 - 'Unknown' for any other suffix.
        """
        suffix = user_input.split()[-1]
        
        if suffix == '-x':
            return 'hexadecimal'
        elif suffix == '-d':
            return 'decimal'
        elif suffix == '-o':
            return 'octal'
        elif suffix == '-b':
            return 'binary'
        elif suffix == '-f':
            return 'float'
        elif suffix == '-dd':
            return 'double'
        else:
            return 'Unknown'