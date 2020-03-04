import cv2 as cv2
import numpy as np
from skimage import exposure,util,io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import glob

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/Celeste/*.png"

imgs = []
#load the images
for file in glob.glob(path):
    img = io.imread(file)
    imgs.append(img)

imgs = np.vstack([img.reshape(1,img.shape[0] * img.shape[1]) for img in imgs])

median = np.median(imgs, axis=0).reshape(1920, 1216)

def normalize(arr):
    arr_min = arr.min()
    arr_max = arr.max()
    return (arr - arr_min) / (arr_max - arr_min)

median = normalize(median)


background_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/bg_celeste.png",median)

bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/bg_celeste.png")
fig = plt.figure(figsize=(10, 10), frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(bg, cmap='Greys_r')
plt.show()


