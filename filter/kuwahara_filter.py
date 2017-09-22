from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import time


def kuwahara_filter(path, mask_size):

    '''
    Applies kuwahara filter on the given image
    :param path:
    :param mask_size: should be odd number, at least 3
    :return: filtered image
    '''

    # variable initialization
    i = Image.open(path)
    image_array = np.asarray(i, dtype=int)
    image_height, image_width = i.size
    half_size = math.floor(mask_size/2)
    resulting_img = np.zeros(image_height * image_width).reshape(image_height, image_width)

    for i in range(half_size, image_height-half_size):

        for j in range(half_size, image_width-half_size):

            # region extraction
            top_left = (image_array[i-half_size:i+1, j-half_size:j+1]).ravel()  # extracts every region from array
            top_right = (image_array[i-half_size:i+1, j:j+half_size+1]).ravel()  # and converts it into 1D array
            bottom_left = (image_array[i:i+half_size+1, j-half_size:j+1]).ravel()
            bottom_right = (image_array[i:i+half_size+1, j:j+half_size+1]).ravel()

            # variance calculation
            tl_var = top_left.var()
            tr_var = top_right.var()
            bl_var = bottom_left.var()
            br_var = bottom_right.var()

            # calculates the min of variances of all regions
            m = np.amin([tl_var, tr_var, bl_var, br_var])

            # finds out which region has the lowest variance, current pixel gets than the mean of that region
            if m == tl_var:
                resulting_img[i, j] = np.mean(top_left)
            elif m == tr_var:
                resulting_img[i, j] = np.mean(top_right)
            elif m == bl_var:
                resulting_img[i, j] = np.mean(bottom_left)
            elif m == br_var:
                resulting_img[i, j] = np.mean(bottom_right)

    return resulting_img

if __name__ == "__main__":
    algorithm_laufzeit = time.time()
    kuwahara_img = kuwahara_filter('lena.png', 5)
    algorithm_laufzeit = time.time()-algorithm_laufzeit
    print(algorithm_laufzeit)
    plt.imshow(kuwahara_img, cmap='gray', interpolation='nearest')
    plt.show()
