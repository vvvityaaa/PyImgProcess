from appJar import gui
from PIL import Image
import numpy as np

from check_if_image_grey import check_if_image_grey
image_set = False

# create a GUI variable
img_process_gui = gui("Image Processing", "1280x1080")
img_process_gui.setGeometry("fullscreen")
img_process_gui.setBg("#c2c6c3")
img_process_gui.setFont(17)

from ImageEdit import ImageEdit
import matplotlib.pyplot as plt


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
    # TODO: comment
    if option == "color proportions":
        piechart = ed_img.color_proportion()
        explode = (0, 0, 0)
        labels = ['Red', 'Green', 'Blue']
        colors = ['red', 'green', 'blue']
        plt.pie(piechart, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.ylabel("Farbanteil")
    elif option == "histogram":
        # plot the result in new window with matplot
        return
    elif option == "cumulative histogram":
        # plot the result in new window with matplot
        return
    elif option == "histogram equalization":
        grey = True  # This value has to be set with the right function
        if not grey:
            # convert with the right function
            return
        temp = Image.fromarray(np.uint8(ed_img.histogram_equalization()))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
        return


def choose_simple(option):
    # TODO: comment
    global showed_image
    if option == "change contrast/brightness":
        grey = check_if_image_grey(showed_image)  # This value has to be set with the right function
        if not grey:
            print("Image should be grey")
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
            print("Image should be grey")
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
    if option == "kuwahara":
        grey = check_if_image_grey(showed_image)  # This value has to be set with the right function
        if not grey:
            print("Image should be grey")
        mask_size = img_process_gui.numberBox("Mask Size", "Set the mask size")
        while mask_size < 3 or mask_size % 2 == 0:
            mask_size = img_process_gui.numberBox("Mask Size", "Set the mask size. It has to be odd and at least 3")

        temp = Image.fromarray(np.uint8(ed_img.kuwahara_filter(mask_size)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "linear filter":
        grey = check_if_image_grey(showed_image)  # This value has to be set with the right function
        if not grey:
            print("Image should be grey")
        mask_size = img_process_gui.numberBox("Mask Size", "Set the mask size")
        while mask_size < 3 or mask_size % 2 == 0:
            mask_size = img_process_gui.numberBox("Mask Size", "Set the mask size. It has to be odd and at least 3")
        temp = Image.fromarray(np.uint8(ed_img.linear_filter(mask_size)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "min filter":
        grey = check_if_image_grey(showed_image)  # This value has to be set with the right function
        if not grey:
            print("Image should be grey")
        region_size = img_process_gui.numberBox("Region Size", "Set the region size")
        while region_size < 3 or region_size % 2 == 0:
            region_size = img_process_gui.numberBox("Region Size", "Set the region size. It has to be odd & at least 3")
        temp = Image.fromarray(np.uint8(ed_img.min_filter(region_size)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "median filter":
        grey = check_if_image_grey(showed_image)  # This value has to be set with the right function
        if not grey:
            print("Image should be grey")
        region_size = img_process_gui.numberBox("Region Size", "Set the region size")
        while region_size < 3 or region_size % 2 == 0:
            region_size = img_process_gui.numberBox("Region Size", "Set the region size. It has to be odd & at least 3")
        temp = Image.fromarray(np.uint8(ed_img.median_filter(region_size)))
        showed_image = 'temporary.png'
        temp.save(showed_image)
        update_image()
    elif option == "max filter":
        grey = check_if_image_grey(showed_image)  # This value has to be set with the right function
        if not grey:
            print("Image should be grey")
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
        temp.save(showed_image)
        update_image()
    elif option == "correlation coefficient":
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
template_matching_name_list = ["champer matching", "correlation coefficient", "distance transformation"]

img_process_gui.addMenuList("Image Statistics", image_statistics_name_list, choose_statistics)
img_process_gui.addMenuList("Simple Operation", simple_operation_name_list, choose_simple)
img_process_gui.addMenuList("Filter Operation", filter_operation_name_list, choose_filter)
img_process_gui.addMenuList("Template Matching", template_matching_name_list, choose_template)

# add Buttons
img_process_gui.addButtons(["Save", "Load"], press)

# start the GUI
img_process_gui.go()
