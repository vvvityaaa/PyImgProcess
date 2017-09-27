from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def histogram(path):

    '''
    Function takes path to the grey_value_image and returns histogram of grey values
    :param path:
    :return:
    '''
    i = Image.open(path)
    array = np.asarray(i, dtype=int)
    histogram_list = np.zeros(255, dtype=int)
    for row in array:
        for element in row:
            histogram_list[element] += 1
    return histogram_list


if __name__ == "__main__":
    histogr = histogram('lena.png')
    plt.bar(np.arange(255),histogr)
    plt.ylabel("Grauwertanzahl")
    plt.show()