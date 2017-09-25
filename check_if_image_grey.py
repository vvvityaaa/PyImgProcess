import numpy as np


def check_if_image_grey(image_2_check):

    '''
    Function should check whether the picture is grey or coloured
    param image_2_check: image that should be checked
    return: should return a boolean; True means it is a grey picture and False means it is a coloured pictures
    '''

    # image array should have only 2 dimensions to be grey image
    if np.ndim(image_2_check) == 2:
        return True
    else:
        return False
