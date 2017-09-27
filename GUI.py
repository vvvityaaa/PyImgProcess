import numpy as np
from PIL import Image
from appJar import gui

from simple_operations.check_if_image_grey import check_if_image_grey

image_set = False
i = 0
# create a GUI variable
img_process_gui = gui("Image Processing", "1280x1080")
img_process_gui.setGeometry("fullscreen")
img_process_gui.setBg("#c2c6c3")
img_process_gui.setFont(17)

from ImageEdit import ImageEdit
import matplotlib.pyplot as plt
import os


#function to update the image
def update_image():
    # TODO: comment
    global ed_img
    global image_set
    if image_set:
        img_process_gui.reloadImage("show_image", showed_image)
        ed_img = ImageEdit(showed_image)
    else:
        img_process_gui.addImage("show_image", showed_image)
        ed_img = ImageEdit(showed_image)
        image_set = True


def create_statistics(titel):

    img_process_gui.startSubWindow(titel, modal=True, blocking=True)
    img_process_gui.addImage(titel, "temporary1.png")
    img_process_gui.showSubWindow(titel)
    os.remove("temporary1.png")
    img_process_gui.destroySubWindow(titel)



# handle events
def press(button):
    # TODO: comment
    global showed_image
    global image_set
    if button == "Save":
        if image_set:
            img_process_gui.saveBox(showed_image)
        else:
            img_process_gui.infoBox("Can't Save Nothing", "You first have to load a picture before you can save one.")
    else:
        showed_image = img_process_gui.openBox()
        update_image()


def choose_statistics(option):
    global i
    global showed_image
    # TODO: comment

    if option == "color proportions":
        # TODO: check if image is coloured
        piechart = ed_img.color_proportion()
        explode = (0, 0, 0)
        labels = ['Red', 'Green', 'Blue']
        colors = ['red', 'green', 'blue']
        plt.pie(piechart, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.ylabel("Farbanteil")
        plt.savefig("temporary1.png")
        create_statistics("Color proportions" + str(i))
        i+=1
    elif option == "histogram":
        histogr = ed_img.histogram()
        plt.bar(np.arange(255), histogr)
        plt.ylabel("Grauwertanzahl")
        plt.savefig("temporary1.png")
        create_statistics("Histogram"+str(i))
        i+=1
        return
    elif option == "cumulative histogram":
        histogr = ed_img.histogram()
        cumul_histogr = ed_img.cumulative_histogram(histogr)
        plt.bar(np.arange(255), cumul_histogr)
        plt.ylabel("Grauwertanzahl")
        plt.savefig("temporary1.png")
        create_statistics("Cumulative histogram"+str(i))
        i+=1
        return
    elif option == "histogram equalization":
        histogr = ed_img.histogram_equalization()
        plt.bar(np.arange(255), histogr)
        plt.xlabel("Equalized histogram")
        plt.savefig("temporary1.png")
        create_statistics("Equalized histogram"+str(i))
        i+=1
        return


def choose_simple(option):
    # TODO: comment
    global showed_image
    if option == "change contrast/brightness":
        grey = check_if_image_grey(showed_image)  # This value has to be set with the right function
        if not grey:
            img_process_gui.infoBox("Can't Edit Image", "You first have to convert it into grey image")
            return
        contrast = img_process_gui.numberBox("Contrast", "Set the contrast modifier")
        brightness = img_process_gui.numberBox("Brightness", "Set the brightness modifier")
        temp = Image.fromarray(np.uint8(ed_img.change_contrast_brightness(contrast, brightness)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "convert to binary":
        threshold = img_process_gui.numberBox("Threshold", "Set the threshold")
        temp = Image.fromarray(np.uint8(ed_img.convert_to_binary(threshold)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "convert to grey":
        wr = img_process_gui.numberBox("Weight of red", "Weight of red color")
        wg = img_process_gui.numberBox("Weight of green", "Weight of green color")
        wb = img_process_gui.numberBox("Weight of blue", "Weight of blue color")
        temp = Image.fromarray(np.uint8(ed_img.convert_to_grey(wr, wg, wb)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "mirror image":
        grey = check_if_image_grey(showed_image)  # This value has to be set with the right function
        if not grey:
            img_process_gui.infoBox("Can't Edit Image", "You first have to convert it into grey image")
        mirror_param = img_process_gui.textBox("Mirror Parameter", "Set the mirror parameter")
        while not (mirror_param == "v" or mirror_param == "h" or mirror_param == "b"):
            mirror_param = img_process_gui.textBox("Mirror Parameter", "The parameter must be v, h or b")
        temp = Image.fromarray(np.uint8(ed_img.mirror_image(mirror_param)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
        return


def choose_filter(option):
    global showed_image
    # TODO: comment

    grey = check_if_image_grey(showed_image)  # This value has to be set with the right function
    if not grey:
        img_process_gui.infoBox("Can't Edit Image", "You first have to convert it into grey image")

    elif option == "kuwahara":
        mask_size = img_process_gui.numberBox("Mask Size", "Set the mask size")
        while mask_size < 3 or mask_size % 2 == 0:
            mask_size = img_process_gui.numberBox("Mask Size", "Set the mask size. It has to be odd and at least 3")

        temp = Image.fromarray(np.uint8(ed_img.kuwahara_filter(mask_size)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "linear filter":
        linear_param = img_process_gui.textBox("Linear Filter Parameter", "Set the linear filter parameter "
                                                                          "(b - boxfilter, g - gaussian filter, g2 - "
                                                                          "gaussian filter in the second grade)")
        while not (linear_param == "b" or linear_param == "g" or linear_param == "g2"):
            linear_param = img_process_gui.textBox("Linear Filter Parameter", "The parameter must be b, g or g2")
        temp = Image.fromarray(np.uint8(ed_img.linear_filter(linear_param)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "min filter":
        region_size = img_process_gui.numberBox("Region Size", "Set the region size")
        while region_size < 3 or region_size % 2 == 0:
            region_size = img_process_gui.numberBox("Region Size", "Set the region size. It has to be odd & at least 3")
        temp = Image.fromarray(np.uint8(ed_img.min_filter(region_size)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "median filter":
        region_size = img_process_gui.numberBox("Region Size", "Set the region size")
        while region_size < 3 or region_size % 2 == 0:
            region_size = img_process_gui.numberBox("Region Size", "Set the region size. It has to be odd & at least 3")
        temp = Image.fromarray(np.uint8(ed_img.median_filter(region_size)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "max filter":
        region_size = img_process_gui.numberBox("Region Size", "Set the region size")
        while region_size < 3 or region_size % 2 == 0:
            region_size = img_process_gui.numberBox("Region Size", "Set the region size. It has to be odd & at least 3")
        temp = Image.fromarray(np.uint8(ed_img.max_filter(region_size)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()


def choose_template(option):
    # TODO: comment
    global showed_image

    if option == "champfer matching":
        template_path = img_process_gui.openBox("Template path")
        temp = Image.fromarray(np.uint8(ed_img.champfer_matching(template_path)))
        showed_image = 'temporary.png'
        update_image()
    elif option == "correlation coefficient":
        grey = check_if_image_grey(showed_image)  # This value has to be set with the right function
        if not grey:
            img_process_gui.infoBox("Can't Edit Image", "You first have to convert it into grey image")
        template_path = img_process_gui.openBox("Template path")
        temp = Image.fromarray(np.uint8(ed_img.correlation_coefficient(template_path)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "distance transformation":
        temp = Image.fromarray(np.uint8(ed_img.distance_transformation()))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()



# add Menu list
image_statistics_name_list = ["color proportions", "histogram", "cumulative histogram", "histogram equalization"]
simple_operation_name_list = ["change contrast/brightness", "convert to binary", "convert to grey",
                              "mirror image"]
filter_operation_name_list = ["kuwahara", "linear filter", "min filter", "median filter", "max filter"]
template_matching_name_list = ["champfer matching", "correlation coefficient", "distance transformation"]

img_process_gui.addMenuList("Image Statistics", image_statistics_name_list, choose_statistics)
img_process_gui.addMenuList("Simple Operations", simple_operation_name_list, choose_simple)
img_process_gui.addMenuList("Filter Operations", filter_operation_name_list, choose_filter)
img_process_gui.addMenuList("Template Matching", template_matching_name_list, choose_template)

# add Buttons
img_process_gui.addButtons(["Save", "Load"], press)

# start the GUI
img_process_gui.go()
