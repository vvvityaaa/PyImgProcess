from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def convert2grey(weight_red, weight_green, weight_blue):

    '''
    Function converts RGB-image to grey_value_image and depends on red, green and blue weight values
    :param weight_red: weight of Red colour, for tv-signals equals 0.299
    :param weight_green: weight of Green colour, for tv-signals equals to 0.587
    :param weight_blue: weight of Blue colour, for tv-signals equals to 0.114
    :return: returns the grey_value_image or plots it
    '''

    i = Image.open('lena.jpg')
    array = np.asarray(I, dtype=np.float32)
    i_grau = weight_red * array[:, :, 0] + weight_green * array[:, :, 1] + weight_blue * array[:, :, 2]
    return i_grau