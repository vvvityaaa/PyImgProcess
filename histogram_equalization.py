from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from histogram import histogram
from cumulative_histogram import cumulative_histogram


def histogram_equalization(path):
    '''
    Calculates equalized histogram of the image.
    Formula: floor(cumulative_histogram(i)*quantity_of_grey_values/(image_height*image_width))
    :param path:
    :return:
    '''
    i = Image.open(path)
    height, width = i.size