from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time


def distance_transformation(path):
    """
    :param path:
    :return:
    SAMPLE MATLAB CODE
    """
    try:
        i = Image.open(path)
        array = np.asarray(i)
    except TypeError:
        return "Parameters seem not to be right"
    except OSError:
        return "This isn't an image"
    array = array[:, :, 0]
    height_img, width_img = array.shape
    distance = (255*np.ones(height_img*width_img)).reshape(height_img, width_img)
    dL = np.zeros(4)
    dR = np.zeros(4)
    for i in range(0, height_img-1):
        for j in range(0, width_img-2):
            if array[i, j] == 255:
                distance[i, j] = 0
    for i in range(1, height_img):
        for j in range(1, width_img-1):
            if distance[i, j] > 0:
                dL[0] = 2 + distance[i-1, j-1]
                dL[1] = 1 + distance[i-1, j]
                dL[2] = 2 + distance[i-1, j+1]
                dL[3] = 1 + distance[i, j-1]
                distance[i, j] = min(dL)
    for i in (0, height_img-2):
        for j in range(0, width_img-2):
            if distance[i, j] > 0:
                dR[0] = 2 + distance[i+1, j+1]
                dR[1] = 1 + distance[i+1, j]
                dR[2] = 2 + distance[i+1, j-1]
                dR[3] = 1 + distance[i, j+1]
                distance[i, j] = min(dR)
    return distance

if __name__ == "__main__":
    algorithm_laufzeit = time.time()
    distance_img = distance_transformation("bin_test.png")
    algorithm_laufzeit = time.time() - algorithm_laufzeit
    print(algorithm_laufzeit)
    if type(distance_img) != str:
        plt.imshow(distance_img, cmap='gray', interpolation='nearest')
        plt.show()
    else:
        print(distance_img)
