from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math


def distance_transformation(path):
    '''

    :param path:
    :return:


    SAMPLE MATLAB CODE
    function [distance] = DistanceTransform(image)
[sizeY, sizeX] = size(image);
distance(1:sizeY,1:sizeX) = 255;
dL =  zeros(1,4);
dR = zeros(1,4);

for i = 1:sizeY
    for j = 1:sizeX
        if (image(i,j) == 1)
            distance(i,j)=0;
        end
    end
end

for i = 2:sizeY
    for j = 2:sizeX-1
        if (distance(i,j)>0)
            dL(1) = 2 + distance(i-1,j-1);
            dL(2) = 1 + distance(i-1,j);
            dL(3) = 2 + distance(i-1,j+1);
            dL(4) = 1 + distance(i,j-1);
            distance(i,j) = min(dL);
        end
    end
end
for i = sizeY-1:1
    for j = sizeX-1:2
        if(distance(i,j)>0)
            dR(1) = 1 + distance(i,j+1);
            dR(2) = 2 + distance(i+1,j-1);
            dR(3) = 1 + distance(i+1,j);
            dR(4) = 2 + distance(i+1,j+1);
            distance(i,j) = min(dL);
        end
    end
end
distance = uint8(distance);
end
    '''