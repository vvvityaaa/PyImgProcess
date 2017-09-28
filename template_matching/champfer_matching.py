from PIL import Image
from template_matching.distance_transformation import distance_transformation
import numpy as np
import matplotlib.pyplot as plt
import time
import math

from open_image import open_image


def champfer_matching(path, template_path):

    '''
    Champfer Matching Algorithm - comparison of binary images based on distance transformation and
    Manhattan-Distance
    :param path: path to the image
    :param template_path: path to the template
    :return: resulting image, minimum values on this image show points, where template can match
    '''

    # initializing image and other helping variables
    image_array = open_image(path)
    template_array = open_image(template_path)
    image_height, image_width = image_array.shape
    template_height, template_width = template_array.shape
    half_template_height = math.floor(template_height / 2)
    half_template_width = math.floor(template_width / 2)
    distance_transformation_matrix = distance_transformation(path)
    resulting_img = np.zeros((image_height-template_height+1) * (image_width-template_width+1)).reshape(image_height-template_height+1, image_width-template_width+1)

    quantity_of_foreground_pix = 0  # quantity of foreground pixels in template
    for i in range(template_height-1):

        for j in range(template_width-1):

            if template_array[i, j] == 0:

                quantity_of_foreground_pix += 1

    # iterating over the image
    for i in range(0, image_height - template_height):

        for j in range(0, image_width - template_width):
            value = 0
            for k in range(template_height):

                for m in range(template_width):
                    # summing up values in distance transformation matrix
                    if template_array[k, m] == 0:
                        value += distance_transformation_matrix[i+k, j+m]
            if quantity_of_foreground_pix != 0:
                resulting_img[i, j] = value/quantity_of_foreground_pix

    return resulting_img


if __name__ == "__main__":
    algorithm_laufzeit = time.time()
    champ_img = champfer_matching('../img/binary_lena.png', '../img/template_binary_lena.png')
    algorithm_laufzeit = time.time() - algorithm_laufzeit
    print(algorithm_laufzeit)
    plt.imshow(champ_img, cmap='gray', interpolation='nearest')
    plt.show()
