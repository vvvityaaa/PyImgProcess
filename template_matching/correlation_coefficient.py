from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import time


def correlation_coefficient(path, template_path):

    '''

    :param path:
    :param template_path:
    :return:
    '''

    # initializing image and other helping variables
    i = Image.open(path)
    image_array = np.asarray(i, dtype=int)
    t = Image.open(template_path)
    template_array = np.asarray(t, dtype=int)
    image_height, image_width = i.size
    template_height, template_width = t.size
    half_template_height = math.floor(template_height/2)
    half_template_width = math.floor(template_width/2)
    resulting_img = np.zeros(image_height * image_width).reshape(image_height, image_width)

    # iterating over the image
    for i in range(half_template_height, image_height - half_template_height):

        for j in range(half_template_width, image_width - half_template_width):

            if template_height % 2 == 1 and template_width % 2 == 1:
                cor_region = image_array[j - half_template_width:j + half_template_width + 1,
                             i - half_template_height:i + half_template_height + 1]
            elif template_height % 2 == 1:
                cor_region = image_array[j - half_template_width:j + half_template_width,
                             i - half_template_height:i + half_template_height + 1]
            elif template_width % 2 == 1:
                cor_region = image_array[j - half_template_width:j + half_template_width + 1,
                             i - half_template_height:i + half_template_height]
            else:
                cor_region = image_array[j - half_template_width:j + half_template_width,
                             i - half_template_height:i + half_template_height]

            covar_region_template = sum(sum(np.cov(cor_region, template_array)))

            variance_region = np.var(cor_region)
            variance_template = np.var(template_array)

            resulting_img[i, j] = covar_region_template/(variance_region*variance_template)

    return resulting_img


if __name__ == "__main__":
    algorithm_laufzeit = time.time()
    cor_img = correlation_coefficient('lena.png', 'template.png')
    algorithm_laufzeit = time.time() - algorithm_laufzeit
    print(algorithm_laufzeit)
    plt.imshow(cor_img, cmap='gray', interpolation='nearest')
    plt.show()



