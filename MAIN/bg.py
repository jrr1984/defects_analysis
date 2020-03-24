import numpy as np #Version: 1.17.3
import skimage.io as io #Version: 0.16.2
import matplotlib.pyplot as plt #Version 3.1.2
from matplotlib_scalebar.scalebar import ScaleBar #Version 0.6.1
from skimage import img_as_float


# path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/Tiles/*.png"
path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/Celeste/*png"
ic = io.ImageCollection(path)
imgs = io.concatenate_images(ic)
print(imgs.shape)
median = np.median(imgs,axis=0).reshape(1920, 1216)
save_img = img_as_float(median)


# background_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/back_NIR.tif",save_img)
background_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/back_Azul.tif",save_img)

bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/back_Azul.tif")
print(len(bg))
print(bg.shape)
fig = plt.figure(1)
# 1 pixel = 0.586 microns
#1216 x 1920 pixels = 712.58 x 1125.12 microns
bg_show = plt.imshow(bg, cmap='Greys_r',extent=(0, 712.58, 0, 1125.12), interpolation='none')
fig.colorbar(bg_show)
#WARNING: according to scalebar documentation:
# "Set dx to 1.0 if the axes image has already been calibrated by setting its extent."
scalebar = ScaleBar(1,'um',location='lower right',fixed_value=100,fixed_units='um',frameon=False)
plt.gca().add_artist(scalebar)
fig.tight_layout()
bins = 500
plt.figure(2)
plt.hist(bg.ravel(), bins=bins, color='Blue', alpha=0.5)
plt.show()


