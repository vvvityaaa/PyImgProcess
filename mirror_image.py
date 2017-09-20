from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def mirror_image(path, parameter='b'):

    '''
    Function mirrors image to vertical or horizontal axis.
    :param path: if parameter == v - image will be mirrored against vertical axis
    if parameter == h - image will be mirrored against horizontal axis
    if parameter == b - image will be mirrored against both axis
    :return:
    '''

    i = Image.open(path)
    array = np.asarray(i, dtype=int)

    if parameter == 'b':
        return np.flip(np.flip(array, 0), 1)
    elif parameter == 'v':
        return np.flip(array, 0)
    elif parameter == 'h':
        return np.flip(array, 1)
    else:
        print("Wrong value for parameter")
        return 0

if __name__ == "__main__":
    mirrored_img = mirror_image('lena.png', 'h')
    plt.imshow(mirrored_img, cmap='gray', interpolation='nearest')
    plt.show()

