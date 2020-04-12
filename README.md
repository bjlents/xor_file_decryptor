# xor_file_decryptor
A useful tool for decrypting files that have been XOR'd. Created by Winning117 for CTF competitions.

Prerequisites:
`sudo apt install python3-pip`
`pip3 install coloredlogs python-magic`

Specific byte mode:
`python3 file_xor.py -f unknown.txt -b 0x89`
This will xor every byte in the file unknown.txt with the byte 0x89. This is useful for when you already know the byte ahead of time.

Brute force mode:
`python3 file_xor.py -f unknown.txt`
This will try every byte value and output files to a folder named `xord_output` within this file directory.


Arguments:
-f or --filename
Use this argument to specify the input file. This argument is required.

-b or --byte
The byte to XOR the file by, accepts either decimal 1-255 or hex 0x01 to 0xFF. If not specified then all possible byte values will be tried.

-d or --decimal
If toggled on then the output files will end in decimal instead of hex. An example would be "unknown_137" instead of the default "unknown_0x89".
