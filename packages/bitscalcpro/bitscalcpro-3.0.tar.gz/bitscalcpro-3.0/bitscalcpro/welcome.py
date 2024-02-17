#!/usr/bin/env python3
# bitscalcpro/welcome.py

class Welcome:

    @staticmethod
    def wc():
        ascii_art = """\033[1;32m
+--------------- Welcome to ---------------------+
        
 ____  _ _        _____      _      _____     v3.0      
|  _ \\(_) |      / ____|    | |    |  __ \\          
| |_) |_| |_ ___| |     __ _| | ___| |__) | __ ___  
|  _ <| | __/ __| |    / _` | |/ __|  ___/ '__/ _ \\ 
| |_) | | |_\\__ \\ |___| (_| | | (__| |   | | | (_) |
|____/|_|\\__|___/\\_____\\__,_|_|\\___|_|   |_|  \\___/ 
                                                            
                                                            
        
+---Comprehensive Numeric Converter & Analyzer---+\033[0m
"""
        print(ascii_art)
        print("\033[1;34mTool Name: BitsCalcPro\033[0m")
        print("\033[1;34mVersion: 3.0\033[0m")
        print("\033[1;34mAuthor Name: MuhammadRizwan\033[0m")
        print("\033[1;34mCountry: India\033[0m")
        print("\033[1;34mTelegram Channel: https://TDOhex.t.me\033[0m")
        print("\033[1;34mTelegram Group: https://TDOhex_Discussion.t.me\033[0m\n")
        print("\033[1;34mEnter: -h or --help to help\033[0m")
        
    @staticmethod
    def display_help():
        print("\nCLA usage: bcp [value] [Flags]")
        print("Interactive mode: [value] [Flags]")
        print("\n  -h, --help\t\tShow this help message and exit")
        print("\npositional arguments:")
        print("  value\t\t\tThe value to perform calculations on\n\t\t\t(float, decimal, hex, octal, or binary)")
        print("\nFlags:")
        print("  -b\t\t\tTo print binary results")
        print("  -d\t\t\tTo print decimal results")
        print("  -x\t\t\tTo print hexadecimal results")
        print("  -o\t\t\tTo print octal results")
        print("  -f\t\t\tTo print float results")
        print("  -dd\t\t\tTo print double results")
        print("\nNotes:")
        print("1. BitsCalcPro support command-line argument and standard input:")
        print("2. Users can pass values both with and without flags.")
        print("\n\nExamples:")
        print("\n$ bcp 1234 - To print all the results of '1234' via the CLA without any flags.")
        print("\n$ bcp 1234 -d - To print the decimal results of '1234' via the CLA with the -d flag.")
        print("\n$ bcp 1234 | sed 's/\x1b\[[0-9;]*m//g' >> output.txt - To export all the results of '1234' to a file named output.txt while removing any color codes.")
        print("\n$ bcp - To run the tool.")
