from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math


def correlation_coefficient(path, template_path):

    '''

    :param path:
    :param template_path:
    :return:


    MATLAB SAMPLE CODE

    function result = GetCorrelationCoefficient(image, template)
%Korrelationskoeffizient = Kovarianz des Bildausschnittes und der Maske/
%                        Varianz des Bildausschnittes und Varianz der Maske
[sizeX, sizeY] = size(image);
[heightT, widthT] = size(template);
result = zeros(sizeX,sizeY);
%Durchschnittswerte von image und template
template_mean = mean(mean(template));
image_mean = mean(mean(image));
for r = (1+heightT):(sizeX-heightT)
    for s = (1+widthT):(sizeY-widthT)
        covar = 0;
        image_variance = 0;
        template_variance = 0;
        for i = 1:heightT
            for j = 1:widthT
                covar = covar + double(image(r+i,s+j)-image_mean)*double(template(i,j)-template_mean);
                image_variance = image_variance + double(image(r+i,s+j)-image_mean)^2;
                template_variance = template_variance + double(template(i,j)-template_mean)^2;
            end
        end
        result(r,s) = 255*(covar/(sqrt(image_variance)*sqrt(template_variance)));
    end
end
result = uint8(result);
end
    '''


