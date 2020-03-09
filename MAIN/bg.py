
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/Tiles/*.png"
ic = io.ImageCollection(path)
imgs = io.concatenate_images(ic)
print(imgs.shape)
median = np.median(imgs,axis=0).reshape(1920, 1216)
print(median)

background_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/back_NIR.tif",median)

bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/back_NIR.tif")
fig = plt.figure(figsize=(10, 10), frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(bg, cmap='Greys_r')
plt.show()


