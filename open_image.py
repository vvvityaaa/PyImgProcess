from PIL import Image
import numpy as np


def open_image(path):

    '''
    Function with try and except to open image in secure mode
    :param path:
    :return:
    '''

    try:

        i = Image.open(path)
        array = np.asarray(i, dtype=int)
        return array

    except TypeError:

        return "Parameters seem not to be right"

    except OSError:

        return "This isn't an image"