import matplotlib.pyplot as plt
import numpy as np
import glob
from skimage import io
from skimage import img_as_float
from matplotlib_scalebar.scalebar import ScaleBar


"""bg = io.imread("C:/Users/juanr/Documents/master_thesis_scratch_and_dig/tesis_tex/Figs/defectosZEISS/img_ideal_2defectos.png")
fig = plt.figure(figsize=(10, 10), frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(bg, cmap='Greys_r')
# bins = 500
plt.figure(2)
# plt.hist(bg.ravel(), bins=bins, color='Blue', alpha=0.5)
plt.hist(bg.ravel(), color='Blue', alpha=0.5,log=True)
plt.xlabel(' Intensidad [u.a.]')
plt.ylabel('Número de píxeles')
# plt.xlim(0,1)
plt.show()"""

img = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/Tiles/Experiment-11_m013_ORG.png")
img = img_as_float(img)
print(np.min(img[480:540,200:260]),np.max(img[480:540,200:260]))
img_final = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/norm/normNIR_13.tif")
print(np.min(img_final[480:540,200:260]),np.max(img_final[480:540,200:260]))
colmap = 'Greys_r'

f, axes = plt.subplots(2, 2)
f.subplots_adjust(hspace=0.4)

img_show = axes[0,0].imshow(img[480:540,200:260],cmap=colmap,extent=(0,35.16,0,35.16), interpolation='none')
f.colorbar(img_show, ax=axes[0,0])
axes[0,0].set_title('i) Defecto imagen original')
scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=20, fixed_units='um', frameon=False, color='Black')
axes[0,0].add_artist(scalebarb)

bg_show = axes[0,1].imshow(img_final[480:540,200:260],cmap=colmap,extent=(0,35.16,0,35.16), interpolation='none')
f.colorbar(bg_show, ax=axes[0, 1])
axes[0, 1].set_title('ii) Defecto imagen final')
scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=20, fixed_units='um', frameon=False, color='Black')
axes[0,1].add_artist(scalebarb)


bins = 50

img_norm_show = axes[1,0].hist(img[480:540,200:260].ravel(),bins, color='Blue', alpha=0.5)
axes[1,0].set_title('iii) Histograma imagen original')

bg_norm_show = axes[1, 1].hist(img_final[480:540,200:260].ravel(),bins, color='Blue', alpha=0.5)
axes[1, 1].set_title('iv) Histograma imagen final')

plt.setp(axes[1, :], xlabel='Intensidad [u.a.]')
plt.setp(axes[1,:], ylabel='Número de píxeles')

plt.setp(axes[0,:], xlabel=' x [\u03BCm]')
plt.setp(axes[0,:], ylabel='y [\u03BCm]')
plt.show()












