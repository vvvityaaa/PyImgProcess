# import the library
from appJar import gui
from PIL import Image
import numpy as np

showed_image = Image
image_set = False


#function to update the image
def update_image():
    global image_set
    if image_set:
        img_process_gui.setImage("show_image", showed_image)
    else:
        img_process_gui.addImage("show_image", showed_image)
        image_set = True


# handle events
def press(button):
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
    if option == "color proportions":
        # plot the result in new window with matplot
        return
    elif option == "histogram":
        # plot the result in new window with matplot
        return
    elif option == "cumulative histogram":
        # plot the result in new window with matplot
        return


def choose_simple(option):
    if option == "change contrast/brightness":
        grey = True  # This value has to be set with the right function
        if not grey:
            # convert with the right function
            return
        contrast = img_process_gui.numberBox("Contrast", "Set the contrast modifier")
        brightness = img_process_gui.numberBox("Brightness", "Set the brightness modifier")
        # showed_image = call the function then updateImg()
    elif option == "convert to binary":
        # showed_image = call the function then updateImg()
        return
    elif option == "convert to grey":
        # showed_image = call the function then updateImg()
        return
    elif option == "histogram equalization":
        grey = True  # This value has to be set with the right function
        if not grey:
            # convert with the right function
            return
        # showed_image = call the function then updateImg()
        return
    elif option == "mirror image":
        grey = True  # This value has to be set with the right function
        if not grey:
            # convert with the right function
            return
        mirror_param = img_process_gui.textBox("Mirror Parameter", "Set the mirror parameter")
        while not (mirror_param == "v" or mirror_param == "h" or mirror_param == "b"):
            region_size = img_process_gui.textBox("Mirror Parameter", "The parameter must be v, h or b")
        # showed_image = call the function then updateImg()
        return


def choose_filter(option):
    if option == "kuwahara":
        grey = True  # This value has to be set with the right function
        if not grey:
            # convert with the right function
            return
        mask_size = img_process_gui.numberBox("Mask Size", "Set the mask size")
        while mask_size < 3 or mask_size % 2 == 0:
            mask_size = img_process_gui.numberBox("Mask Size", "Set the mask size. It has to be odd and at least 3")
        # showed_image = call the function then updateImg()
        return
    elif option == "linear filter":
        grey = True  # This value has to be set with the right function
        if not grey:
            # convert with the right function
            return
        mask_size = img_process_gui.numberBox("Mask Size", "Set the mask size")
        while mask_size < 3 or mask_size % 2 == 0:
            mask_size = img_process_gui.numberBox("Mask Size", "Set the mask size. It has to be odd and at least 3")
        # showed_image = call the function then updateImg()
        return
    elif option == "min filter":
        grey = True  # This value has to be set with the right function
        if not grey:
            # convert with the right function
            return
        region_size = img_process_gui.numberBox("Region Size", "Set the region size")
        while region_size < 3 or region_size % 2 == 0:
            region_size = img_process_gui.numberBox("Region Size", "Set the region size. It has to be odd & at least 3")
        # showed_image = call the function then updateImg()
        return
    elif option == "median filter":
        grey = True  # This value has to be set with the right function
        if not grey:
            # convert with the right function
            return
        region_size = img_process_gui.numberBox("Region Size", "Set the region size")
        while region_size < 3 or region_size % 2 == 0:
            region_size = img_process_gui.numberBox("Region Size", "Set the region size. It has to be odd & at least 3")
        # showed_image = call the function then updateImg()
        return
    elif option == "max filter":
        grey = True  # This value has to be set with the right function
        if not grey:
            # convert with the right function
            return
        region_size = img_process_gui.numberBox("Region Size", "Set the region size")
        while region_size < 3 or region_size % 2 == 0:
            region_size = img_process_gui.numberBox("Region Size", "Set the region size. It has to be odd & at least 3")
        # showed_image = call the function then updateImg()
        return


def choose_template(option):
    if option == "champer matching":
        return
    elif option == "correlation coefficient":
        return
    elif option == "distance transformation":
        return


# create a GUI variable
img_process_gui = gui("Image Processing", "1280x1080")
img_process_gui.setBg("#c2c6c3")
img_process_gui.setFont(17)

# add Menu list
image_statistics_name_list = ["color proportions", "histogram", "cumulative histogram"]
simple_operation_name_list = ["change contrast/brightness", "convert to binary", "convert to grey", "histogram equalization", "mirror image"]
filter_operation_name_list = ["kuwahara", "linear filter", "min filter", "median filter", "max filter"]
template_matching_name_list = ["champer matching", "correlation coefficient", "distance transformation"]
img_process_gui.addMenuList("Image Statistics", image_statistics_name_list, choose_statistics)
img_process_gui.addMenuList("Simple Operation", simple_operation_name_list, choose_simple)
img_process_gui.addMenuList("Filter Operation", filter_operation_name_list, choose_filter)
img_process_gui.addMenuList("Template Matching", template_matching_name_list, choose_template)

# add Buttons
img_process_gui.addButtons(["Save", "Load"], press)


# start the GUI
img_process_gui.go()
