import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.absolute()))

import numpy as np
from ..dumper.dumper import Dumper

def main():
    dumper = Dumper()

    memory = np.loadtxt("image.txt", dtype=np.uint8)

    try:
        dumper.run("dump.txt", memory, 0x010, 0x037)

    except KeyboardInterrupt:
        print("[INFO] Ending Program")


if __name__ == '__main__':
    main()
