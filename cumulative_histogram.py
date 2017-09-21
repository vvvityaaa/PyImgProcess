from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from histogram import histogram


def cumulative_histogram(histogr):

    '''
    Creates cumulative histogram of the image. It means histogram, where all previos values of the value are summed up.
    :param histogram:
    :return: list with values of cumulative histogram
    '''

    new_histogram = []
    accumulator = 0
    for value in histogr:
        accumulator += value
        new_histogram.append(accumulator)
    return new_histogram

if __name__ == "__main__":
    histogr = histogram('lena.png')
    cumul_histogr = cumulative_histogram(histogr)
    plt.bar(np.arange(255), cumul_histogr)
    plt.ylabel("Grauwertanzahl")
    plt.show()
