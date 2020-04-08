# python3

import argparse
import os
import sys
import logging
import shutil
import magic # pip3 install python-magic
import coloredlogs # pip3 install coloredlogs

logger = None

def setup_logger():
    """
    Sets up the logger
    """
    logging.basicConfig(filename='xor_file_decryptor.log', level=logging.DEBUG)
    global logger
    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG', milliseconds=True) # the level specified here sets what level logs will be shown in the console
    return logger

def create_xord_file(input_file, output_file, byte_to_xor):
    """
    Creates an XOR'd file by XORing it with the specified byte (byte is in hex)
    """
    input_file_as_bytes = bytearray(open(input_file, 'rb').read())
    for i in range(len(input_file_as_bytes)):
        input_file_as_bytes[i] ^= byte_to_xor
    open(output_file, 'wb').write(input_file_as_bytes)
    file_type = magic.from_file(output_file)
    if file_type != "data":
        logger.info(f"XORing with the byte '{byte_to_xor}' created a '{file_type}' file!")

def validate_input_file(input_file):
    """
    Ensures that the input file exists
    """
    location_of_file_to_xor = os.path.abspath(os.path.expanduser(input_file))
    if not os.path.exists(location_of_file_to_xor):
        logger.error(f"There doesn't seem to be a file named '{location_of_file_to_xor}'!")
        sys.exit(1)
    return location_of_file_to_xor

def main():
    logger = setup_logger()
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', "--filename", required=True, help="The file to be XOR'd")
    parser.add_argument('-b', "--byte", help="The byte to XOR the file by, accepts either decimal 1-255 or hex 0x01 to 0xFF. If not specified then all bytes will be tried.")
    parser.add_argument('-o', "--outputfile", help="The name of the file to output to")
    args = parser.parse_args()

    location_of_file_to_xor = validate_input_file(args.filename)

    this_file_location = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(this_file_location, "xord_output")

    if os.path.exists(output_folder):
        logger.debug(f"Removing the '{output_folder}' folder so that we can have clean output for this session...")
        shutil.rmtree(output_folder)
        logger.debug(f"Successfully removed the '{output_folder}' folder.")
    logger.debug(f"Creating a folder for output at '{output_folder}'...")
    os.mkdir(output_folder)
    logger.debug(f"Successfully created a folder for output at '{output_folder}'...")

    if args.byte:
        byte_as_string = args.byte
        byte_as_decimal = None
        if byte_as_string.startswith("0x"):
            byte_as_decimal = int(byte_as_string, 16)
            if byte_as_decimal < 1 or byte_as_decimal > 255:
                logger.error(f"The specified byte '{byte_as_string}' should be between 0x01 and 0xFF!")
                sys.exit(1)
        else:
            byte_as_decimal = int(byte_as_string)
            if byte_as_decimal < 1 or byte_as_decimal > 255:
                logger.error(f"The specified byte '{byte_as_string}' should be between 1 and 255!")
                sys.exit(1)

        if "." in args.filename:
            xord_file_name = args.filename.split(".")[0] + "_xor_" + byte_as_string
        else:
            xord_file_name = args.filename + "_xor_" + byte_as_string
        xord_file_name = os.path.join(output_folder, xord_file_name)

        logger.info(f"XORing the file '{location_of_file_to_xor}' by the byte '{byte_as_string}'...")
        create_xord_file(input_file=location_of_file_to_xor, output_file=xord_file_name, byte_to_xor=byte_as_decimal)
        logger.info(f"Successfully output to the file '{xord_file_name}'.")
    else:
        logger.info("A specific byte wasn't specified, so we're going to brute force it...")
        for num in range(1, 256):
            if "." in args.filename:
                xord_file_name = args.filename.split(".")[0] + "_xor_" + str(num)
            else:
                xord_file_name = args.filename + "_xor_" + str(num)
            xord_file_name = os.path.join(output_folder, xord_file_name)
            create_xord_file(input_file=location_of_file_to_xor, output_file=xord_file_name, byte_to_xor=num)
        logger.info(f"Successfully created 255 files in '{output_folder}'.")


if __name__ == "__main__":
    main()
