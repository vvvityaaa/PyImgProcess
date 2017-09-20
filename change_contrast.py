from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def change_contrast(path, a, b):
    '''
    Changes contrast of the given image with parameters a and b. Formula b*image[i,j]+a
    :param path:
    :param a:
    :param b:
    :return:
    '''