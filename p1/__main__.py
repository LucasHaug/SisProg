import numpy as np

from .loader.loader import Loader

def main():
    loader = Loader()

    memory = np.zeros(4096, dtype=np.uint8)

    try:
        loader.run("mem.txt", memory)

        np.savetxt("image.txt", memory, fmt='%02X')
    except KeyboardInterrupt:
        print("[INFO] Ending Program")


if __name__ == '__main__':
    main()
