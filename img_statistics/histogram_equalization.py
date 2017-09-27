from math import floor

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from img_statistics.histogram import histogram

from img_statistics.cumulative_histogram import cumulative_histogram


def histogram_equalization(path):
    '''
    Calculates equalized histogram of the image.
    Formula: floor(cumulative_histogram(i)*quantity_of_grey_values/(image_height*image_width))
    :param path:
    :return:
    '''
    i = Image.open(path)
    image_height, image_width = i.shape
    size = image_height*image_width
    hist = histogram(path)
    quantity_of_grey_values = len(hist)
    cumul_hist = cumulative_histogram(hist)
    equalized_histogram = []
    for value in cumul_hist:
        equalized_histogram.append(floor(value*quantity_of_grey_values/size))
    return equalized_histogram

if __name__ == "__main__":
    histogr = histogram_equalization('lena.png')
    plt.bar(np.arange(255), histogr)
    plt.xlabel("Equalized histogram")
    plt.show()
