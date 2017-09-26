from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def convert_to_grey(path, weight_red=0.299, weight_green=0.587, weight_blue=0.114):

    '''
    Function converts RGB-image to grey_value_image and depends on red, green and blue weight values
    :param path: the picture's path
    :param weight_red: weight of Red colour, for tv-signals equals 0.299
    :param weight_green: weight of Green colour, for tv-signals equals to 0.587
    :param weight_blue: weight of Blue colour, for tv-signals equals to 0.114
    :return: returns the grey_value_image or plots it
    '''
    try:
        i = Image.open(path)
        array = np.asarray(i, dtype=np.float32)
        i_grau = weight_red * array[:, :, 0] + weight_green * array[:, :, 1] + weight_blue * array[:, :, 2]
        return i_grau
    except TypeError:
        return "Parameters seem not to be right"
    except OSError:
        return "This isn't an image"

if __name__ == "__main__":
    grey_img = convert_to_grey('lena.jpg', 0.2125, 0.7154, 0.072)
    if type(grey_img) != str:
        plt.imshow(grey_img, cmap='gray', interpolation='nearest')
        plt.show()
    else:
        print(grey_img)
