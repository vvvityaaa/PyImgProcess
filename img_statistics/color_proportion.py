from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from open_image import open_image


def color_proportion(path):
    """
    The function creates a piechart that shows the portions of red, green and blue in the picture
    :param path: path to the picture
    :return: list with values for the piechart
    """
    image_array = open_image(path)

    color_proportion_list = []
    # appends sum of values in red dimension
    color_proportion_list.append(sum(sum(image_array[:, :, 0])))
    # appends sum of values in green dimension
    color_proportion_list.append(sum(sum(image_array[:, :, 1])))
    # appends sum of values in blue dimension
    color_proportion_list.append(sum(sum(image_array[:, :, 2])))
    return color_proportion_list


if __name__ == "__main__":
    piechart = color_proportion('../img/lena.jpg')
    if type(piechart) != str:
        explode = (0, 0, 0)
        labels = ['Red', 'Green', 'Blue']
        colors = ['red', 'green', 'blue']
        plt.pie(piechart, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.ylabel("Color proportions")
        plt.show()
    else:
        print(piechart)
