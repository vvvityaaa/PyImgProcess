from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math


def distance_transformation(path):
    """
    :param path:
    :return:
    SAMPLE MATLAB CODE
    """
    try:
        i = Image.open(path)
        array = np.asarray(i, dtype=np.float32)
    except TypeError:
        return "Parameters seem not to be right"
    except OSError:
        return "This isn't an image"
    size_x, size_y = array.shape
    distance = (255*np.ones(size_x*size_y)).reshape(size_x, size_y)
    dL = np.zeros(4)
    dR = np.zeros(4)
    for i in range(1, size_x):
        for j in range(1, size_y):
            if array[i, j] == 1:
                distance[i, j] = 0
    for i in range(2, size_y):
        for j in range(2, size_x-1):
            if distance[i, j] > 0:
                dL[0] = 2 + distance[i-1, j-1]
                dL[1] = 1 + distance[i-1, j]
                dL[2] = 2 + distance[i-1, j+1]
                dL[3] = 1 + distance[i, j-1]
                distance[i, j] = min(dL)
    for i in range(size_y-1, 1):
        for j in range(size_x-1, 2):
            if distance[i, j] > 0:
                dR[0] = 2 + distance[i-1, j-1]
                dR[1] = 1 + distance[i-1, j]
                dR[2] = 2 + distance[i-1, j+1]
                dR[3] = 1 + distance[i, j-1]
                distance[i, j] = min(dR)
    return distance

if __name__ == "__main__":
    distance_img = distance_transformation('lena.png')
    if type(distance_img) != str:
        plt.imshow(distance_img, cmap='gray', interpolation='nearest')
        plt.show()
    else:
        print(distance_img)
