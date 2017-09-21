from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math


def linear_filter(path, mask):
    """
    Filters the image on the given path with linear filter mask. (Folien 3 Seite 46 und Folien 4 Seite 27)
    :param path:
    :param mask:
    :return: filtered image
    """
    try:
        image = Image.open(path)
        img_array = np.asarray(image, dtype=np.float32)
    except TypeError:
        return "Parameters seem not to be right"
    except OSError:
        return "This isn't an image"
    sizeX, sizeY = img_array.shape
    height_m, width_m = mask.shape
    border_height = int(height_m/2)
    border_width = int(width_m/2)
    result = np.zeros(sizeX*sizeY).reshape(sizeX, sizeY)

    #The factor for normalisation is set
    factor = sum(sum(mask))

    for i in range(1+border_height, sizeX-border_height):
        for j in range(1+border_width, sizeY-border_width):
            value = 0.0
            y = 1
            for k in range(i-border_height, i+border_height):
                x = 1
                for m in range(j-border_width,j+border_width):
                    #the real calculation; multiplication with the mask
                    value = value + img_array[k, m]*mask[y, x]
            if factor != 0:
                value = value/factor
            result[i, j] = value
    return result

"""
SAMPLE CODE FrOM MATLAB:
function result = ImageFiltering(image,mask)
[sizeX, sizeY] = size(image);
[heightM, widthM] = size(mask);
borderHeight = floor(heightM/2);
borderWidth = floor(widthM/2);
factor =  0;
result = zeros(sizeX,sizeY);
%Hier wird die Normalisierung durchgeführt
for i=1:heightM
    for j=1:widthM
        factor = factor + mask(i,j);
    end
end
%4 Schleifen, die ersten beiden gehen durch das Bild durch
%die letzen beiden durch die Maske
for i = (1+borderHeight):(sizeX-borderHeight)
    for j = (1+borderWidth):(sizeY-borderWidth)
        value = 0.0;
        y = 1;
        for k = (i-borderHeight):(i+borderHeight)
            x = 1;
            for m = (j-borderWidth):(j+borderWidth)
                %die eigentliche Berechnung, Multiplikation des Pixelwertes
                %mit der Maske
                value = value + double(image(k,m)*mask(y,x));
                x = x + 1;
            end
            y = y + 1;
        end
        if factor~=0
            value = value/factor;
        end
        result(i,j) = value;
    end
end
%image muss von den double zu den uint8 Format wechseln, um das Bild
%richtig darstellen zu können
result = uint8(result);
end


if __name__ == "__main__":"""
if __name__ == "__main__":
    result_img = linear_filter('lena.png', np.arange(9).reshape(3, 3))
    if type(result_img) != str:
        plt.imshow(result_img, cmap='gray', interpolation='nearest')
        plt.show()
    else:
        print(result_img)
