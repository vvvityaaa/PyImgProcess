from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import time

from open_image import open_image


def linear_filter(path, mask):

    '''
    Filters the image on the given path with linear filter mask.
    :param path:
    :param mask:
    :return: filtered image
    '''

    image_array = open_image(path)
    size_x, size_y = image_array.shape
    height_m, width_m = mask.shape
    border_height = math.floor(height_m/2)
    border_width = math.floor(width_m/2)
    result = np.zeros(size_x*size_y).reshape(size_x, size_y)

    # The factor for normalisation is set
    factor = sum(sum(mask))

    for i in range(border_height, size_x-border_height):
        for j in range(border_width, size_y-border_width):
            # region extraction
            region = image_array[i-border_height:i+border_height+1, j-border_width:j+border_width+1]
            # multiplication of region with mask and summing up of its values
            value = sum(sum(region*mask))
            # normalization of value
            if factor != 0:
                value = value/factor
            result[i, j] = value
    return result


if __name__ == "__main__":
    algorithm_laufzeit = time.time()
    result_img = linear_filter('../img/lena_511_476.png', np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],
                                                                    [1,4,6,4,1],[4,16,24,16,4]]))
    algorithm_laufzeit = time.time() - algorithm_laufzeit
    print(algorithm_laufzeit)
    if type(result_img) != str:
        plt.imshow(result_img, cmap='gray', interpolation='nearest')
        plt.show()
    else:
        print(result_img)
