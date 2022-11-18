import numpy as np

from PIL import Image
import sys

import matplotlib.pyplot as plt

#from readimg import ReadImage


def FreqLaplacian( f ):
    return g

if __name__=='__main__':
    f = ReadImage('./lena.bmp')

    g = FreqLaplacian(f)

    plt.imshow( g, cmap='gray')
    plt.show()
