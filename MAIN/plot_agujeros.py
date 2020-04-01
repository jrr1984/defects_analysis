from skimage.filters import threshold_yen
from skimage import io,measure,img_as_float,morphology
from skimage.measure import regionprops_table
from skimage.color import label2rgb
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
import pandas as pd
import cv2


img = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/BandaVerde/norm/normVerde_84.tif")
img = img_as_float(img)
thresh = threshold_yen(img)
binary = img <= thresh
masked_binary = ndimage.binary_fill_holes(binary,structure=np.ones((5,5)))
hols = masked_binary.astype(int) - binary
# cleaned_binary = morphology.remove_small_objects(masked_binary, 2)
label_image = measure.label(masked_binary)
proplist = ['area','equivalent_diameter']
props = regionprops_table(label_image, intensity_image=img, properties=proplist)
props_df = pd.DataFrame(props)
print('defects_df')
print(props_df)

lab = measure.label(hols)
cleaned_holes = morphology.remove_small_objects(lab, min_size=47,connectivity=8)
hole_label = measure.label(cleaned_holes)

props_holes = regionprops_table(hole_label, intensity_image=img, properties=proplist)
props_holes_df = pd.DataFrame(props_holes)
print('holes')
print(props_holes_df)

"""
colmap = 'Greys_r'
bins = 1000
f, axes = plt.subplots(2, 2, figsize=(20, 20))
f.subplots_adjust(hspace=0.4)
# [510:1050,500:1150],extent=(0,316.44,0,380.9)
img_show = axes[0,0].imshow(img,cmap=colmap, interpolation='none')
# img_show = axes[0,0].imshow(img,cmap=colmap, interpolation='none')
f.colorbar(img_show, ax=axes[0,0])
axes[0,0].set_title('a) Imagen Normalizada')
scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='Black')
axes[0,0].add_artist(scalebarb)

axes[1,0].hist(img[510:1050,500:1150].ravel(),bins,log=True)
# axes[1,0].imshow(img,cmap=colmap, interpolation='none')
axes[1, 0].set_title('b) Histograma Imagen Normalizada')
axes[1,0].axvline(thresh, color='r')


# img_norm_show = axes[0, 1].imshow(binary[510:1050,500:1150],extent=(0,316.44,0,380.9), cmap=colmap, interpolation='none')
img_norm_show = axes[0, 1].imshow(binary, cmap=colmap, interpolation='none')
axes[0, 1].set_title('c) Imagen Binaria Defectos')
scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='w')
axes[0,1].add_artist(scalebarw)


# axes[1, 1].imshow(cleaned_holes[510:1050,500:1150],extent=(0,316.44,0,380.9), cmap=colmap, interpolation='none')
axes[1, 1].imshow(hols, cmap=colmap, interpolation='none')
axes[1, 1].set_title('d) Imagen Binaria Agujeros')
scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='w')
axes[1,1].add_artist(scalebarw)
plt.setp(axes[0, :], xlabel=' x [\u03BCm]')
plt.setp(axes[0, :], ylabel='y [\u03BCm]')
plt.setp(axes[1, 1], xlabel=' x [\u03BCm]')
plt.setp(axes[1, 1], ylabel='y [\u03BCm]')
plt.show()
"""
colmap = 'Greys_r'
bins = 1000
f, axes = plt.subplots(2, 2, figsize=(20, 20),sharex=True,sharey=True)
f.subplots_adjust(hspace=0.4)

# img_show = axes[0,0].imshow(img[510:1050,500:1150],extent=(0,316.44,0,380.9),cmap=colmap, interpolation='none')
img_show = axes[0, 0].imshow(img, cmap=colmap, interpolation='none')
f.colorbar(img_show, ax=axes[0, 0])
axes[0, 0].set_title('a) Imagen Normalizada')
scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False,
                     color='Black')
axes[0, 0].add_artist(scalebarb)

# axes[1, 0].hist(img.ravel(), bins, log=True)
axes[1,0].imshow(masked_binary, cmap=colmap, interpolation='none')
axes[1, 0].set_title('b) Histograma Imagen Normalizada')
# axes[1, 0].axvline(thresh, color='r')

# img_norm_show = axes[0, 1].imshow(binary[510:1050,500:1150],extent=(0,316.44,0,380.9), cmap=colmap, interpolation='none')
img_norm_show = axes[0, 1].imshow(binary, cmap=colmap, interpolation='none')
axes[0, 1].set_title('c) Imagen Binaria')
scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='w')
axes[0, 1].add_artist(scalebarw)

axes[1, 1].imshow(cleaned_holes, cmap=colmap, interpolation='none')
axes[1, 1].set_title('d) Agujeros tapados')
scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='w')
axes[1, 1].add_artist(scalebarw)
axes[1, 1].set_xticks([])
axes[1, 1].set_yticks([])
plt.setp(axes[0, :], xlabel=' x [\u03BCm]')
plt.setp(axes[0, :], ylabel='y [\u03BCm]')
plt.setp(axes[1, 1], xlabel=' x [\u03BCm]')
plt.setp(axes[1, 1], ylabel='y [\u03BCm]')
plt.show()
