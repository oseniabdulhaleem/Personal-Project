# import os to delete file later if specifed
import os

# import time
import time

# Import Argumentparse
import argparse


# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


def main():

    parser = argparse.ArgumentParser(prog="qrc",
                                     description="Generate qrcode from a value and delete later")

    parser.add_argument(
        "link", type=str, help="input the data to be --qrcoded--")
    parser.add_argument("-time", type=float, default=0,
                        help="How long data should be in the system in mins. Defaults to 0 if it is to be stored permanently in the system")

    data = parser.parse_args().link
    timeBeforeDelete = parser.parse_args().time

    # String which represents the QR code
    s = "my_link"

    # Generate QR code
    url = pyqrcode.create(data)

    # save as filename
    filename = 'myqr.png'

    # Create and save the png file
    if timeBeforeDelete == 0:
        url.png(filename, scale=6)
    else:
        url.png(filename, scale=6)
        time.sleep(timeBeforeDelete * 60)
        os.remove(os.path.join(os.getcwd(), filename))

    return


if __name__ == '__main__':
    main()

# Create and save the svg file naming "myqr.svg"

# url.svg("myqr.svg", scale=8)
