from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from open_image import open_image


def convert_to_binary(path, threshold):
    '''
    Converts an image to binary(2-value) image with a given threshold
    :param path:
    :param threshold: grey value which divides, all values that are greater than it will get 255 value,
    all the values less than it will get 0 value
    :return:
    '''

    image_array = open_image(path)

    for i in range(len(image_array)):

        for j in range(len(image_array[i])):

            value = image_array[i, j]
            # checks if value is greater or less than threshold
            if value > threshold:
                image_array[i, j] = 255
            else:
                image_array[i, j] = 0
    return image_array


if __name__ == "__main__":
    binary_img = convert_to_binary('../img/lena.png', 150)
    plt.imshow(binary_img, cmap='gray', interpolation='nearest')
    plt.show()