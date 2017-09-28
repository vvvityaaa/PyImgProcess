from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

from open_image import open_image


def distance_transformation(path):

    """
    Distance transformation of the binary image based on Manhattan Distance (city block distance)

    :param path: path to the image
    :return: distance transformation array of the image
    SAMPLE MATLAB CODE
    """
    image_array = open_image(path)
    height_img, width_img = image_array.shape
    distance = (255*np.ones(height_img*width_img)).reshape(height_img, width_img)
    dL = np.zeros(4)  # saving manhattan distance values
    dR = np.zeros(4)  # saving manhattan distance values

    # initializing distance of foreground pixels with 0
    for i in range(0, height_img-1):

        for j in range(0, width_img-2):

            if image_array[i, j] == 255:
                distance[i, j] = 0

    # iteration over the image LEFT -> RIGHT
    for i in range(1, height_img):

        for j in range(1, width_img-1):

            if distance[i, j] > 0:
                dL[0] = 2 + distance[i-1, j-1]
                dL[1] = 1 + distance[i-1, j]
                dL[2] = 2 + distance[i-1, j+1]
                dL[3] = 1 + distance[i, j-1]
                # calculation minimum of distance values of the region
                distance[i, j] = min(dL)

    # iteration over the image RIGHT -> LEFT
    for i in (0, height_img-2):

        for j in range(width_img-1, 0):

            if distance[i, j] > 0:
                dR[0] = 2 + distance[i+1, j+1]
                dR[1] = 1 + distance[i+1, j]
                dR[2] = 2 + distance[i+1, j-1]
                dR[3] = 1 + distance[i, j+1]
                # calculation minimum of distance values of the region
                distance[i, j] = min(dR)
    return distance

if __name__ == "__main__":
    algorithm_laufzeit = time.time()
    distance_img = distance_transformation("../img/binary_lena.png")
    algorithm_laufzeit = time.time() - algorithm_laufzeit
    print(algorithm_laufzeit)
    if type(distance_img) != str:
        plt.imshow(distance_img, cmap='gray', interpolation='nearest')
        plt.show()
    else:
        print(distance_img)
