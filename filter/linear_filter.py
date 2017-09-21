from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def linear_filter(path, mask):
    '''
    Filters the image on the given path with linear filter mask. (Folien 3 Seite 46 und Folien 4 Seite 27)
    :param path:
    :param mask:
    :return: filtered image


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
    '''


if __name__ == "__main__":