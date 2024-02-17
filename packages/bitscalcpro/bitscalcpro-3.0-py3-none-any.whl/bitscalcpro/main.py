#!/usr/bin/env python3
# bitscalcpro/main.py

import sys
import time
from bitscalcpro.welcome import Welcome
from bitscalcpro.validator import Validator
from bitscalcpro.print_info import PrintInfo

class Main:
    """
    Main class for the bitscalcpro application.

    Methods:
    - main(): Main method to execute the application.
    - main_loop(): Main loop for the interactive part of the application, prompting user input and displaying results.
    """

    @staticmethod
    def main():
        """
        Entry point for the bitscalcpro application.
        Initiates the application based on command line arguments or starts the main loop for interactive use.
        """
        
        if len(sys.argv) > 1:
            if sys.argv[1] == "--help" or sys.argv[1] == "-h":
                Welcome.display_help()
                sys.exit()
            Welcome.wc()
            time.sleep(2)
            args = sys.argv[1:]
            suffix = Validator.suffix_representation(args[-1])
            if suffix != 'Unknown':
                user_input = Validator.input_validation(''.join(args[:-1]))
                PrintInfo.print_bits_info2(user_input, suffix)
                PrintInfo.print_result2(user_input, suffix)
            else:
                user_input = Validator.input_validation(''.join(args))
                PrintInfo.print_bits_info(user_input)
                PrintInfo.print_result(user_input)
        else:
            Welcome.wc()
        Main.main_loop()
    
    @staticmethod
    def main_loop():
        """
        Main loop for the interactive part of the bitscalcpro application.
        Prompts the user to enter a value (float, decimal, hex, octal, or binary),
        validates the input, and prints information about the bits as well as the result.
        """
        while True:
            user_input = input("\033[93m\nEnter a value (float, decimal, hex, octal, or binary) or press Enter to terminate the program: \033[0m")
            if not user_input:
                print("\033[1;34m\nProgram terminated.\033[0m")
                break
            elif user_input.strip() in ["--help", "-h"]:
                Welcome.display_help()
                break
            parts = user_input.split()
            try:
                suffix = Validator.suffix_representation(parts[-1])
                if suffix == 'Unknown':
                    user_input = Validator.input_validation(user_input)
                    if user_input is not None:
                        PrintInfo.print_bits_info(user_input)
                        PrintInfo.print_result(user_input)
                else:
                    suffix_removed = ' '.join(parts[:-1])
                    user_input = Validator.input_validation(suffix_removed)
                    if user_input is not None:
                        PrintInfo.print_bits_info2(user_input, suffix)
                        PrintInfo.print_result2(user_input, suffix)
            except IndexError:
                pass
if __name__ == "__main__":
    Main.main()