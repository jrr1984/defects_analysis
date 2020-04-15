from skimage.filters import threshold_yen
from skimage import io,measure,img_as_float
from scipy import ndimage
from matplotlib_scalebar.scalebar import ScaleBar
from skimage import io,measure,img_as_float,morphology
from skimage.measure import regionprops_table
from skimage.color import label2rgb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

pixels_to_microns = 0.586
proplist = ['equivalent_diameter','area']
hole_thresh = 0.975

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Azul/norm/*.tif"

data= []
holes_data = []
i=0

for file in sorted(glob.glob(path)):
    img = io.imread(file)
    img = img_as_float(img)
    contours = measure.find_contours(img, hole_thresh)
    contour_image = np.zeros(img.shape)
    for c in contours:
        c = np.round(c).astype(int)
        coords = (c[:, 0], c[:, 1])
        contour_image[coords] = 1

    hole_binary = contour_image >= hole_thresh
    cont_img = ndimage.binary_fill_holes(hole_binary)
    cleaned_holes = morphology.remove_small_objects(cont_img, min_size=47,connectivity=8)
    hole_label = measure.label(cleaned_holes)

    if not hole_label.any():
        pass
    else:
        props_holes = regionprops_table(hole_label, intensity_image=img, properties=proplist)
        holes_df = pd.DataFrame(props_holes)
        holes_df['img'] = i
        holes_data.append(holes_df)
        print('holes_df')
        print(holes_df)
    i += 1
    print(file, i)

    colmap = 'Greys_r'
    bins = 1000
    f, (ax1,ax2) = plt.subplots(1, 2, figsize=(20, 20),sharex=True,sharey=True)
    f.subplots_adjust(hspace=0.4)

    img_show = ax1.imshow(img, cmap=colmap, interpolation='none')
    f.colorbar(img_show, ax=ax1)
    ax1.set_title('Imagen Normalizada')
    scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False,
                         color='Black')
    ax1.add_artist(scalebarb)


    ax2.imshow(cleaned_holes, cmap=colmap, interpolation='none')
    ax2.set_title('Agujeros detectados')
    scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='w')
    ax2.add_artist(scalebarw)
    ax2.set_xticks([])
    ax2.set_yticks([])
    plt.setp((ax1,ax2), xlabel=' x [\u03BCm]')
    plt.setp((ax1,ax2), ylabel='y [\u03BCm]')
    plt.show()