import numpy as np

class Memory():
    def __init__(self, size) -> None:
        self.array = np.zeros(size, dtype=np.uint8)


    def __getitem__(self, index):
        return self.array[index]


    def __setitem__(self, index, value):
        self.array[index] = value


    def clear(self):
        self.array *= 0


    def display(self):
        np.savetxt("image.txt", self.array, fmt='%02X')

