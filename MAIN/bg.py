import numpy as np #Version: 1.17.3
import skimage.io as io #Version: 0.16.2
import matplotlib.pyplot as plt #Version 3.1.2
from matplotlib_scalebar.scalebar import ScaleBar #Version 0.6.1
from skimage import img_as_float
import seaborn as sns

plt.rcParams["font.size"] = "15"
# path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/Tiles/*.png"
path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/Celeste/*png"
ic = io.ImageCollection(path)
imgs = io.concatenate_images(ic)
imgs = img_as_float(imgs)
print(imgs.shape)
mean = np.mean(imgs,axis=0).reshape(1920, 1216)
print(mean)
median = np.median(imgs,axis=0).reshape(1920, 1216)
print(median)

# background_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/back_NIR.tif",median)
# background_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/back_meanAzul.tif",mean)

# bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/back_Azul.tif")
fig = plt.figure(1)
# 1 pixel = 0.586 microns
#1216 x 1920 pixels = 712.58 x 1125.12 microns
bg_show = plt.imshow(mean, cmap='Greys_r',extent=(0, 712.58, 0, 1125.12), interpolation='none')
fig.colorbar(bg_show)
plt.xlabel(' x [\u03BCm]')
plt.ylabel('y [\u03BCm]')
plt.title('Valor Medio')
#WARNING: according to scalebar documentation:
# "If the the axes image has already been calibrated by setting its extent, set dx to 1.0."
scalebar = ScaleBar(1,'um',location='lower right',fixed_value=200,fixed_units='um',frameon=False,color ='w')
plt.gca().add_artist(scalebar)
fig.tight_layout()

fig = plt.figure(2)
bg_show = plt.imshow(median, cmap='Greys_r',extent=(0, 712.58, 0, 1125.12), interpolation='none')
fig.colorbar(bg_show)
plt.xlabel(' x [\u03BCm]')
plt.ylabel('y [\u03BCm]')
plt.title('Mediana')
#WARNING: according to scalebar documentation:
# "If the the axes image has already been calibrated by setting its extent, set dx to 1.0."
scalebar = ScaleBar(1,'um',location='lower right',fixed_value=200,fixed_units='um',frameon=False,color ='w')
plt.gca().add_artist(scalebar)
fig.tight_layout()


def return_intersection(hist_1, hist_2):
    minima = np.minimum(hist_1, hist_2)
    intersection = np.true_divide(np.sum(minima), np.sum(hist_2))
    return intersection


bins = np.linspace(0.735, 0.86, 100)
sns.set(font_scale=1.5);
plt.figure(3)
sns.distplot(median.ravel(),hist=True,norm_hist=False,bins=bins,kde=True,label='Mediana')
sns.distplot(mean.ravel(),hist=True,norm_hist=False,bins=bins,kde=True,label='Valor Medio')
plt.xlabel(' Intensidad [u.a.]')
plt.ylabel('Número de píxeles')
plt.legend(loc='upper right')
plt.show()


