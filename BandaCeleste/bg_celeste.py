import cv2 as cv2
import numpy as np
from skimage import exposure,util,img_as_uint
import skimage.io as io
import matplotlib.pyplot as plt
path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/Celeste/*.png"
# path = "C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Banda2scenes/*.png"
ic = io.ImageCollection(path)
imgs = io.concatenate_images(ic)
print(imgs.shape)
median = np.median(imgs,axis=0).reshape(1920, 1216)
print(median)

# im = exposure.rescale_intensity(median, out_range='float')
# im = normalize(median)
# save = img_as_uint(median)
background_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/back.tif",median)

bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/back.tif")
# print(bg)
fig = plt.figure(figsize=(10, 10), frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(bg, cmap='Greys_r')
plt.show()


