from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import time

def linear_filter(path, mask):

    '''
    Filters the image on the given path with linear filter mask. (Folien 3 Seite 46 und Folien 4 Seite 27)
    :param path:
    :param mask:
    :return: filtered image
    '''

    try:
        image = Image.open(path)
        img_array = np.asarray(image, dtype=np.float32)
    except TypeError:
        return "Parameters seem not to be right"
    except OSError:
        return "This isn't an image"
    size_x, size_y = img_array.shape
    height_m, width_m = mask.shape
    border_height = math.floor(height_m/2)
    border_width = math.floor(width_m/2)
    result = np.zeros(size_x*size_y).reshape(size_x, size_y)

    # The factor for normalisation is set
    factor = sum(sum(mask))

    for i in range(border_height, size_x-border_height+1):
        for j in range(border_width, size_y-border_width+1):
            value = 0
            x = 0  # Variable to iterate over a mask
            for k in range(i-border_height, i+border_height):
                y = 0  # Variable to iterate over a mask
                for m in range(j-border_width, j+border_width):
                    # the real calculation; multiplication with the mask
                    value = value + img_array[k, m]*mask[x, y]
                    y += 1
                x += 1
            if factor != 0:
                value = value/factor
            result[i, j] = value
    return result


if __name__ == "__main__":
    algorithm_laufzeit = time.time()
    result_img = linear_filter('lena.png', np.arange(49).reshape(7, 7))
    algorithm_laufzeit = time.time() - algorithm_laufzeit
    print(algorithm_laufzeit)
    if type(result_img) != str:
        plt.imshow(result_img, cmap='gray', interpolation='nearest')
        plt.show()
    else:
        print(result_img)
