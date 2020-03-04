import cv2 as cv2
import numpy as np
from skimage import exposure,util,io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import glob

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/Tiles/*.png"

bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/background_notinverted.png")
# bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/bg_celeste.png")
# bg = rgb2gray(bg)
bg = util.img_as_ubyte(bg)
# bg_mat = np.matrix(bg)
bg_mean = np.mean(bg)


def normalize(arr):
    arr_min = arr.min()
    arr_max = arr.max()
    return (arr - arr_min) / (arr_max - arr_min)
i=0
#load the images
for file in glob.glob(path):
    i+=1
    img = io.imread(file)
    # img = rgb2gray(img)
    img = util.img_as_ubyte(img)
    # img_mat = np.matrix(img)
    img_mean = np.mean(img)
    # result = np.divide(bg,img)
    bg_norm = bg*img_mean
    img_norm = img*bg_mean
    result = img_norm - bg_norm
    result = result - np.min(result)
    result = result/np.max(result)
    norm = normalize(result)
    # norm = util.img_as_ubyte(result)
    norm_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/norm/normNIR_{}.png".format(str(i)), norm)






