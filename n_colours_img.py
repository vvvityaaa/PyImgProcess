from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

'''
Function should check wether the picture ist grey oder coloured
param image_2_check: image that should be checked
return: should return a boolean; True means it is a grey picture and false means it is a coloured pictures
'''


def check_if_image_grey(image_2_check):
    return np.ndim(image_2_check)  # If the picture is grey, than the third dimension should have the length 1


def n_colours_img(path, colours):
    '''
    Function should convert grey_value_image to n-coloured image.
    :param path: path to the image, colours: array with colours
    :return: should return or just plot resulting image.
    '''

    image_2_change = Image.open(path)
    if check_if_image_grey(image_2_change):
        max_value = np.max(image_2_change)
        min_value = np.min(image_2_change)
        step_count = len(colours)
        step_width = (max_value - min_value) / step_count
        for step in range(max_value, min_value, step_count):
            changed_image = [step for pixel in image_2_change if ((pixel - step) < step_width) & ((pixel - step) > 0)]
            return changed_image
    else:
        print("The picture should be grey")
changed = n_colours_img("C:\\Users\\Artur\\Pictures\\lena.png", [100, 200, 345])
print(changed)
