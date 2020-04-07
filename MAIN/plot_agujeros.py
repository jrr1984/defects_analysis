from skimage.filters import threshold_yen,threshold_triangle,threshold_isodata
from skimage import io,measure,img_as_float,morphology
from skimage.measure import regionprops_table
from skimage.color import label2rgb
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
import pandas as pd
import cv2
pixels_to_microns = 0.586
proplist = ['equivalent_diameter','area']

img = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/AZUL/norm/normAzul_112.tif")
img = img_as_float(img)
thresh = threshold_yen(img)
binary = img <= thresh
binarymenos = img <= (thresh-0.1*thresh)

masked_binary =ndimage.binary_fill_holes(binary)
masked_binarymenos =ndimage.binary_fill_holes(binarymenos)
label_image = measure.label(masked_binary,connectivity=2)
label_imagemenos = measure.label(masked_binarymenos,connectivity=2)
hols = masked_binary.astype(int) - binary
hols_var = masked_binarymenos.astype(int) - binarymenos
lab = measure.label(hols,connectivity=2)
lab_var = measure.label(hols_var, connectivity=2)
cleaned_holes = morphology.remove_small_objects(lab, connectivity=2)
cleaned_holes_var = morphology.remove_small_objects(lab_var, connectivity=2)
label_final = morphology.remove_small_objects(label_image, min_size=100)
label_finalmenos = morphology.remove_small_objects(label_imagemenos, min_size=100)
props = regionprops_table(label_final, intensity_image=img, properties=proplist)
propsmenos = regionprops_table(label_finalmenos, intensity_image=img, properties=proplist)
props_df = pd.DataFrame(props)
props_dfmenos = pd.DataFrame(propsmenos)
print('defects_df')
print(props_df)
print('MENOS')
print(props_dfmenos)
print('ERROR')
print((props_df-props_dfmenos)/2)


colmap = 'Greys_r'
bins = 1000
f, (ax1,ax2,ax3) = plt.subplots(1, 3, figsize=(20, 20),sharey=True,sharex=True)
f.subplots_adjust(hspace=0.4)
# [510:1050,500:1150],extent=(0,316.44,0,380.9)
img_show = ax1.imshow(img,cmap=colmap,extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
# ax1.imshow(masked_binary,cmap='Greens',extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
# ax1.imshow(masked_binarymenos,cmap='winter',extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
# img_show = axes[0,0].imshow(img,cmap=colmap, interpolation='none')
# f.colorbar(img_show, ax=ax1)
ax1.set_title('a) Imagen Normalizada')
scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=10, fixed_units='um', frameon=False, color='Black')
ax1.add_artist(scalebarb)


ax2.imshow(masked_binary,cmap='Reds',extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
ax2.imshow(masked_binarymenos,cmap='Blues',extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
ax2.imshow(cleaned_holes,cmap='winter',extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
ax2.imshow(cleaned_holes_var,cmap='autumn',extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
ax2.set_title('b) Imagen Binaria*')
scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=10, fixed_units='um', frameon=False, color='Black')
ax2.add_artist(scalebarw)


ax3.imshow(masked_binary,cmap='Reds',extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
ax3.imshow(masked_binarymenos,cmap='Blues',extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
ax3.imshow(cleaned_holes,cmap='winter',extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
ax3.imshow(cleaned_holes_var,cmap='autumn',extent=(0, 712.58, 0, 1125.12), interpolation='none',alpha=0.5)
ax3.set_title('c) Zoom Borde')
scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=5, fixed_units='um', frameon=False, color='Black')
ax3.add_artist(scalebarw)
ax3.get_shared_x_axes().remove(ax3)
ax3.get_shared_y_axes().remove(ax3)

plt.setp(ax1, xlabel=' x [\u03BCm]')
plt.setp(ax1, ylabel='y [\u03BCm]')
plt.setp(ax2, xlabel=' x [\u03BCm]')
plt.setp(ax2, ylabel='y [\u03BCm]')
plt.setp(ax3, xlabel=' x [\u03BCm]')
plt.setp(ax3, ylabel='y [\u03BCm]')


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
"""
