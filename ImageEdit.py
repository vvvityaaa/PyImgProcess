import numpy as np

from simple_operations.check_if_image_grey import check_if_image_grey
from simple_operations.convert_to_binary import convert_to_binary
from simple_operations.convert_to_grey import convert_to_grey
from simple_operations.mirror_image import mirror_image
from simple_operations.change_contrast_brightness import change_contrast_brightness

from img_statistics.color_proportion import color_proportion
from img_statistics.histogram import histogram
from img_statistics.histogram_equalization import histogram_equalization
from img_statistics.cumulative_histogram import cumulative_histogram

from filter.kuwahara_filter import kuwahara_filter
from filter.linear_filter_old import linear_filter
from filter.max_filter import max_filter
from filter.median_filter import median_filter
from filter.min_filter import min_filter

from template_matching.champfer_matching import champfer_matching
from template_matching.correlation_coefficient import correlation_coefficient
from template_matching.distance_transformation import distance_transformation


class ImageEdit(object):

    '''
    Class for image editing, which takes path as argument during initialization.
    Then you can apply different methods on that class object.
    '''

    def __init__(self, path):
        self.path = path

    def change_contrast_brightness(self, con, br):
        return change_contrast_brightness(self.path, con, br)

    def check_if_image_grey(self):
        return check_if_image_grey(self.path)

    def color_proportion(self):
        return color_proportion(self.path)

    def convert_to_binary(self, thresh):
        return convert_to_binary(self.path, thresh)

    def convert_to_grey(self, wr=0.299, wg=0.587, wb=0.114):
        return convert_to_grey(self.path, wr, wg, wb)

    def cumulative_histogram(self, his):
        return cumulative_histogram(his)

    def histogram(self):
        return histogram(self.path)

    def histogram_equalization(self):
        return histogram_equalization(self.path)

    def mirror_image(self, par):
        return mirror_image(self.path, par)

    def kuwahara_filter(self, mask_size):
        return kuwahara_filter(self.path,mask_size)

    def linear_filter(self, param):
        # depending on different parameters passed to the textField of GUI
        # you have either a box filter or a gaussian filter
        if param == 'b':
            mask = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        elif param == 'g':
            mask = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
        elif param == 'g2':
            mask = np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [1, 4, 6, 4, 1], [4, 16, 24, 16, 4]])
        else:
            raise ValueError
        return linear_filter(self.path, mask)

    def max_filter(self, rs):
        return max_filter(self.path, rs)

    def min_filter(self, rs):
        return min_filter(self.path, rs)

    def median_filter(self, rs):
        return median_filter(self.path, rs)

    def champfer_matching(self, tp):
        return champfer_matching(self.path, tp)

    def distance_transformation(self):
        return distance_transformation(self.path)

    def correlation_coefficient(self, tp):
        return correlation_coefficient(self.path, tp)