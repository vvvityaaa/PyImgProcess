from PIL import Image
import numpy as np
from open_image import open_image


def check_if_image_grey(path):

    '''
    Function should check whether the picture is grey or coloured
    param path: path to the image that should be checked
    return: should return a boolean; True means it is a grey picture and False means it is a coloured pictures
    '''

    image_array = open_image(path)

    # image array should have only 2 dimensions to be grey image
    if np.ndim(image_array) == 2:
        return True
    else:
        return False
