from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def kuwahara_filter(path, mask_size):

    '''
    Applies kuwahara filter on the given image
    :param path:
    :param mask_size: should be odd number, at least 3
    :return: filtered image

    SAMPLE CODE IN MATLAB
    function result = KuwaharaFilter(image,maskSize)
%Kuwahara Filter:
%Teile Umgebung in 4 Regionen
%Auswahl der Region mit geringster Varianz
%Mittelwert dieser Region wird in den jeweiligen Pixel gespeichert

[sizeX, sizeY] = size(image);
halfSize = floor(maskSize/2);

for i = (1+halfSize):(sizeX-halfSize)
    for j = (1+halfSize):(sizeY-halfSize)
        %Arrays von 4 Regionen zu dem Pixel(i,j)
        top_left = image(i-halfSize:i,j-halfSize:j);
        top_right = image(i-halfSize:i,j:j+halfSize);
        bottom_left = image(i:i+halfSize,j-halfSize:j);
        bottom_right = image(i:i+halfSize,j:j+halfSize);
        %Mittelwerte der 4 Regionen
        avg_tl = sum(sum(top_left))/numel(top_left);
        avg_tr = sum(sum(top_right))/numel(top_right);
        avg_bl = sum(sum(bottom_left))/numel(bottom_left);
        avg_br = sum(sum(bottom_right))/numel(bottom_right);

        %Berechnung der Varianz der vier Regionen
        var_tl = 0;
        var_tr = 0;
        var_bl = 0;
        var_br = 0;
        for m = i-halfSize:i
            for k = j-halfSize:j
                var_tl = var_tl+(double(image(m,k))-avg_tl)^2;
            end
        end
        var_tl=var_tl/numel(top_left);

        for m = i-halfSize:i
            for k = j:j+halfSize
                var_tr = var_tr+(double(image(m,k))-avg_tr)^2;
            end
        end
        var_tr=var_tr/numel(top_right);

        for m = i:i+halfSize
            for k = j-halfSize:j
                var_bl = var_bl+(double(image(m,k))-avg_bl)^2;
            end
        end
        var_bl=var_bl/numel(bottom_left);

        for m = i:i+halfSize
            for k = j:j+halfSize
                var_br = var_br+(double(image(m,k))-avg_br)^2;
            end
        end
        var_br=var_br/numel(bottom_right);

        %Auswahl der Region mit der geringsten Varianz und
        %Zuweisung des Mittelwertes dieser Region dem Pixel
        m = min([var_tr,var_tl,var_br,var_bl])
        if m==var_tr
            image(i,j)=avg_tr;
        elseif m==var_tl
            image(i,j)=avg_tl;
        elseif m==var_br
            image(i,j)=avg_br;
        elseif m==var_bl
            image(i,j)=avg_bl;
        end

    end
end
result=image;
end
    '''


if __name__ == "__main__":