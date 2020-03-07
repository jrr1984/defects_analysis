import cv2 as cv2
import numpy as np
from skimage import exposure,util,img_as_uint
import skimage.io as io
import matplotlib.pyplot as plt
path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/Tiles/*.png"

ic = io.ImageCollection(path)
imgs = io.concatenate_images(ic)
print(imgs.shape)
median = np.median(imgs,axis=0).reshape(1920, 1216)
print(median.shape)
def normalize(arr):
    arr_min = arr.min()
    arr_max = arr.max()
    return (arr - arr_min) / (arr_max - arr_min)
# im = exposure.rescale_intensity(median, out_range='float')
im = normalize(median)
save = img_as_uint(im)
background_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/bg_celeste.png",save)

bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/bg_celeste.png").astype(np.uint16)
# print(bg)
fig = plt.figure(figsize=(10, 10), frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(bg, cmap='Greys_r')
plt.show()


