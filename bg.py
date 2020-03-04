import cv2 as cv2
import numpy as np
from skimage import exposure,util,io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import glob

path = "C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Banda2scenes/*.png"

imgs = []
#load the images
for file in glob.glob(path):
    img = io.imread(file)
    imgs.append(img)

# Convert images to 4d ndarray, size(n, nrows, ncols, 3)
imgs = np.asarray(imgs)
# Take the median over the first dim
median = np.median(imgs, axis=0)

def normalize(arr):
    arr_min = arr.min()
    arr_max = arr.max()
    return (arr - arr_min) / (arr_max - arr_min)

# median = normalize(median)

# median = util.img_as_ubyte(median)

background_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Banda2scenes/bgnow.png",median)

bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Banda2scenes/bgnow.png")
fig = plt.figure(figsize=(10, 10), frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(bg, cmap='Greys_r')
plt.show()



