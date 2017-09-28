from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import time
import exmod

from open_image import open_image


def median_filter(path, region_size):

    '''
    Values for every pixel equals to the median of all values in the region
    :param path: path to the image
    :param region_size: size of the region that will be extracted and its median will be calculated
    :return: resulting image
    '''

    # initializing image and other helping variables
    image_array = open_image(path)
    image_height, image_width = image_array.shape
    half_size = math.floor(region_size/2)
    resulting_img = np.zeros(image_height * image_width).reshape(image_height, image_width)
    # iterating over the image
    for i in range(half_size, image_height-half_size):

        for j in range(half_size, image_width-half_size):
            # extraction of region of the given size and calculation of its median
            region = (image_array[i-half_size:i+half_size+1, j-half_size:j+half_size+1]).ravel()
            # median is calculated in C-extension module exmod
            resulting_img[i, j] = exmod.median(list(region))

    return resulting_img


if __name__ == "__main__":
    algorithm_laufzeit = time.time()
    median_img = median_filter('../img/lena_noise.png', 3)
    algorithm_laufzeit = time.time() - algorithm_laufzeit
    print(algorithm_laufzeit)
    plt.imshow(median_img, cmap='gray', interpolation='nearest')
    plt.show()
