from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def prozent_of_img(path):
    """
    The function creates a piechart that shows the portions of red, green and blue in the picture
    :param path: path to the picture
    :return: list with values for the piechart
    """
    try:
        i = Image.open(path)
        array = np.asarray(i, dtype=np.float32)
        value_list = []
        value_list.append(sum(sum(array[:, :, 0])))
        value_list.append(sum(sum(array[:, :, 1])))
        value_list.append(sum(sum(array[:, :, 2])))
        return value_list
    except TypeError:
        return "The params seems not to be rigth"
    except OSError:
        return "This isn't an image"
    except IndexError:
        return "The image isn't colored"
if __name__ == "__main__":
    piechart = portionsofcolours('lena.jpg')
    if type(piechart) != str:
        explode = (0,0,0)
        labels = ['Red', 'Green', 'Blue']
        colors = ['red', 'green', 'blue']
        plt.pie(piechart, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
        plt.ylabel("Farbanteil")
        plt.show()
    else:
        print(piechart)
