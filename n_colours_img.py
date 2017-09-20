from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

'''
Function should check wether the picture ist grey oder coloured
param image_2_check: image that should be checked
return: should return a boolean; True means it is a grey picture and false means it is a coloured pictures
'''

def check_if_image_grey(image_2_check):
    return len(image_2_check[0:0:]) == 1 #If the picture is grey, than the third dimension should have the length 1

def n_colours_img(path, colours):

    '''
    Function should convert grey_value_image to n-coloured image.
    :param path: path to the image, colours: array with colours
    :return: should return or just plot resulting image.
    '''
    i = Image.open(path)
    if(check_if_grey(i) == True):
        max_Value = np.max(i)
        min_Value = np.min(i)
        step_count = len(colours)
        step_width = (max_value-min_Value)/step_count
        for step in range(max_vaule, min_value, step_count):
            for 
            if(((i - step)<step_width) & ((i-step)>0))):
                
    else:
        print("The picture should be grey")
