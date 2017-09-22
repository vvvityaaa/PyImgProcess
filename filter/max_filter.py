from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math


def max_filter(path, region_size):
    '''
        Values for every pixel equals to the max of all values in the region
        :param path: path to the image
        :param region_size: size of the region that will be extracted and its median will be calculated
        :return: resulting image
        '''

    # initializing image and other helping variables
    i = Image.open(path)
    image_array = np.asarray(i, dtype=int)
    image_height, image_width = i.size
    half_size = math.floor(region_size / 2)
    resulting_img = np.zeros(image_height * image_width).reshape(image_height, image_width)
    # iterating over the image
    for i in range(half_size, image_height - half_size):

        for j in range(half_size, image_width - half_size):
            # extraction of region of the given size and calculation of its median
            region = (image_array[i - half_size:i + half_size + 1, j - half_size:j + half_size + 1]).ravel()
            resulting_img[i, j] = np.max(region)

    return resulting_img


if __name__ == "__main__":
    max_img = max_filter('lena_noise.png', 3)
    plt.imshow(max_img, cmap='gray', interpolation='nearest')
    plt.show()
