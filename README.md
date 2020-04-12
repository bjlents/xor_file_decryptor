
# xor_file_decryptor
A useful tool for decrypting files that have been XOR'd.
Created by Winning117 for CTF competitions.

**Prerequisites:**<br>
`sudo apt install python3-pip`<br>
`pip3 install coloredlogs python-magic`<br>

**Specific byte mode:**<br>
`python3 file_xor.py -f unknown.txt -b 0x89`<br>
This will xor every byte in the file unknown.txt with the byte 0x89. This is useful for when you already know the byte ahead of time.<br>

**Brute force mode:**<br>
`python3 file_xor.py -f unknown.txt`<br>
This will try every byte value and output files to a folder named `xord_output` within this file directory.<br>

**Arguments:**<br>
-f or --filename<br>
Use this argument to specify the input file. This argument is required.<br>

-b or --byte<br>
The byte to XOR the file by, accepts either decimal 1-255 or hex 0x01 to 0xFF. If not specified then all possible byte values will be tried.<br>

-d or --decimal<br>
If toggled on then the output files will end in decimal instead of hex. An example would be "unknown_137" instead of the default "unknown_0x89".<br>
