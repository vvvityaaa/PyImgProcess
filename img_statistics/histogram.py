from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from open_image import open_image


def histogram(path):

    '''
    Function takes path to the grey_value_image and returns histogram of grey values
    :param path:
    :return:
    '''
    image_array = open_image(path)

    histogram_list = np.zeros(255, dtype=int)

    for row in image_array:

        for element in row:

            histogram_list[element] += 1

    return histogram_list


if __name__ == "__main__":
    histogr = histogram('../img/lena.png')
    plt.bar(np.arange(255),histogr)
    plt.ylabel("Grauwertanzahl")
    plt.show()