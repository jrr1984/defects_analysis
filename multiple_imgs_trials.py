import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
from skimage import measure,color,io,util,filters,feature
from skimage.measure import regionprops_table
from skimage.color import rgb2gray,grey2rgb
from skimage.segmentation import clear_border
import pandas as pd

pixels_to_microns = 0.586
proplist = ['label','area','convex_area','filled_area','major_axis_length','minor_axis_length','perimeter',
            'equivalent_diameter','extent']

path = "C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Bandanorm/*.png"




for file in glob.glob(path):
    ig1 = io.imread(file)
    img1 = grey2rgb(ig1)
    img1 = util.img_as_ubyte(img1)
    img = util.invert(ig1)
    img = util.img_as_ubyte(img)

    # ret1,thresh = cv2.threshold(img,10,255,cv2.THRESH_BINARY +cv2.THRESH_OTSU)
    ret,thresh = cv2.threshold(img,15,255,cv2.THRESH_BINARY)
    # f, (ax0, ax1) = plt.subplots(1, 2, figsize=(10, 5))
    # ax0.imshow(img1, cmap='gray')
    # ax1.imshow(thresh, cmap='gray')
    # plt.show()
    kernel = np.ones((1,1),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)
    # opening = clear_border(opening) #descarta los 'recortados' de los bordes
    # f, (ax0, ax1) = plt.subplots(1, 2, figsize=(10, 5))
    # ax0.imshow(img1, cmap='gray')
    # ax1.imshow(opening, cmap='gray')
    # plt.show()

    #removesmallobjects, img + minsize

    sure_bg = cv2.dilate(opening,kernel,iterations=1)
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,3)
    ret2,sure_fg = cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)
    ret3,markers = cv2.connectedComponents(sure_fg)
    markers += 10
    markers[unknown==255] = 0
    markers = cv2.watershed(img1,markers)
    props = regionprops_table(markers, intensity_image=img, properties=proplist)
    data = pd.DataFrame(props)
    data['equivalent_diameter'] = data['equivalent_diameter'] * pixels_to_microns
    data['area'] = data['area'] * pixels_to_microns * pixels_to_microns
    # img1[markers==-1] = [0,255,255]
    # img2 = color.label2rgb(markers,bg_label=0)
    # f, (ax0, ax1) = plt.subplots(1, 2, figsize=(10, 5))
    # ax0.imshow(img1, cmap='gray')
    # ax1.imshow(img2, cmap='gray')
    # plt.show()






