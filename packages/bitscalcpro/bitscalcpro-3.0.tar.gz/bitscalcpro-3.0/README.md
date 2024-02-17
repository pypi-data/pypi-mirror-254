<!-- BitsCalcPro -->

<p align="center"><b>BitsCalcPro</b></p>
<p align="center"><b>Comprehensive Numeric Converter & Analyzer</b></p>

##

<h3><p align="left">Disclaimer:</p></h3>

<i>Welcome to <b>BitsCalcPro</b>

BitsCalcPro is a comprehensive numeric converter and analyzer tool.

It facilitates seamless conversion between different numeric formats, including decimal, binary, octal, hexadecimal, float, and double. With its versatile capabilities.

BitsCalcPro offers precise conversions, detailed bit size insights, and support for byte order reversal.</i>

##

### Features:

- Bits size calculation:
  - Provides the number of bits required to represent the input value in binary, octal, hexadecimal, float, and double.

- Decimal conversions:
  - Converts decimal values to hexadecimal (normal and reversed order), octal, and binary.

- Binary conversions:
  - Converts binary values to decimal, hexadecimal (normal and reversed order), octal, float, and double.

- Octal conversions:
  - Converts octal values to decimal, hexadecimal (normal reversed order), binary, float, and double.

- Hexadecimal conversions:
  - Converts hexadecimal values to decimal, octal, binary, float, and double. Supports both normal and reversed modes.

- Float conversions:
  - Converts float values to hexadecimal (normal and reversed order), octal, binary, and double.

- Double conversions:
  - Converts double values to hexadecimal (normal and reversed order), octal, binary, and actual decimal.

These features make your tool versatile, allowing for seamless conversions between different number systems.

##

### Why BitsCalcPro?

- Input Validation:
  - Automatic validation to fix prefixes and spaces in input values.
  - Automatic determination the possible formats for the input values then printing the results for each possible format.

- Byte Order Swap:
  - Specialized feature supporting byte order reversal for 16-bit, 32-bit, and 64-bit values.

- IEEE 754 Conversion Support:
  - Comprehensive support for IEEE 754 floating-point format, covering both single-precision (float) and double-precision (double) values.

##

### Installation:

- To quick Installation via Pip:
  ```bash
  pip install bitscalcpro
  ```

- To custom build, Clone the repository and install the package locally:
  ```bash
  git clone https://github.com/muhammadrizwan87/bitscalcpro.git
  cd bitscalcpro
  python -m build
  pip install .
  ``` 
##

### Usage:  
- Please run `bcp --help` to show the usage.
```
CLA usage: bcp [value] [Flags]
Interactive mode: [value] [Flags]

  -h, --help            Show this help message and exit

positional arguments:
  value                 The value to perform calculations on
                        (float, decimal, hex, octal, or binary)

Flags:
  -b                    To print binary results
  -d                    To print decimal results
  -x                    To print hexadecimal results
  -o                    To print octal results
  -f                    To print float results
  -dd                   To print double results

Notes:
1. BitsCalcPro support command-line argument and standard input:
2. Users can pass values both with and without Flags.


Examples:

$ bcp 1234 - To print all the results of "1234" via the CLA without any flags.

$ bcp 1234 -d - To print the decimal results of "1234" via the CLA with the -d flag.

$ bcp 1234 | sed 's/\x1b\[[0-9;]*m//g' >> output.txt - To export all the results of "1234" to a file named output.txt while removing any color codes.

$ bcp - To run the tool.
```
##

### Follow Me on Telegram:
[Dimension of TDO](https://TDOhex.t.me)

[Useful Patches](https://Android_Patches.t.me)

<!-- // -->
