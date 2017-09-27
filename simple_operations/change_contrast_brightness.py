from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def change_contrast_brightness(path, contrast=1, brightness=0):

    '''
    Changes contrast and brightness of the given image with parameters contrast and brightness.
    Formula contrast*image[i,j]+brightness

    :param path: path to the image
    :param contrast: contrast of the new image, default 1
    :param brightness: brightness of the new image, default 0
    :return: new image
    '''

    i = Image.open(path)
    image_array = np.asarray(i, dtype=int)

    for i in range(len(image_array)):

        for j in range(len(image_array[i])):

            value = contrast*image_array[i, j] + brightness

            # if values go out of boundaries they have to be normalized
            if value < 0:
                image_array[i, j] = 0
            elif value > 255:
                image_array[i, j] = 255
            else:
                image_array[i, j] = contrast*image_array[i, j] + brightness

    return image_array

if __name__ == "__main__":
    contrasted_img = change_contrast_brightness('lena.png', -1, 255)
    plt.imshow(contrasted_img, cmap='gray', interpolation='nearest')
    plt.show()
