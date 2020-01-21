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

# Stack the reshaped images (rows) vertically:
imgs = np.vstack([img.reshape(3,img.shape[0] * img.shape[1]) for img in imgs])

median = np.median(imgs, axis=0).reshape(1920, 1216)

median = util.img_as_ubyte(median)

background_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Banda2scenes/background.png",median)

bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Banda2scenes/background.png")
fig = plt.figure(figsize=(10, 10), frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(bg, cmap='Greys_r')
plt.show()


