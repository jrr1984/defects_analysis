from skimage.filters import threshold_yen
from skimage import io,measure,img_as_float
from skimage.measure import regionprops_table
from skimage.color import label2rgb
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
import pandas as pd
import glob

pixels_to_microns = 0.586
proplist = ['area','convex_area','filled_area','major_axis_length','minor_axis_length',
            'perimeter','equivalent_diameter','extent']

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Azul/norm/*.tif"

data= []
i=0

for file in glob.glob(path):
    img = io.imread(file)
    img = img_as_float(img)
    thresh = threshold_yen(img)
    binary = img <= thresh
    # masked_binary =ndimage.binary_fill_holes(binary)
    label_image = measure.label(binary)


    props = regionprops_table(label_image, intensity_image=img, properties=proplist)
    props_df = pd.DataFrame(props)
    print(props_df)
    print(file,i)
    props_df['img'] = i
    i += 1
    data.append(props_df)
"""
    image_label_overlay = label2rgb(label_image, image=img, bg_label=0)
    # f, (ax0, ax1,ax2) = plt.subplots(1, 3, figsize=(10, 5),sharex=True,sharey=True)
    # ax0.imshow(img, cmap='gray')
    # ax1.imshow(image, cmap='gray')
    # ax2.imshow(masked_binary, cmap='gray')
    # plt.show()

    #plot image process step by step comparison
    colmap = 'Greys_r'
    bins = 1000
    f, axes = plt.subplots(2, 2, figsize=(20, 20))
    f.subplots_adjust(hspace=0.4)

    img_show = axes[0,0].imshow(img[1690:1750,880:960],cmap=colmap, interpolation='none')
    f.colorbar(img_show, ax=axes[0,0])
    axes[0,0].set_title('a) Imagen Normalizada')
    scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=10, fixed_units='um', frameon=False, color='Black')
    axes[0,0].add_artist(scalebarb)

    axes[1,0].hist(img.ravel(),bins,log=True)
    axes[1, 0].set_title('b) Histograma Imagen Normalizada')
    axes[1,0].axvline(thresh, color='r')


    img_norm_show = axes[0, 1].imshow(binary, cmap=colmap,extent=(0, 712.58, 0, 1125.12), interpolation='none')
    # f.colorbar(img_norm_show,ticks=range(1), ax=axes[0, 1])
    axes[0, 1].set_title('c) Imagen Binaria')
    scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=10, fixed_units='um', frameon=False, color='w')
    axes[0,1].add_artist(scalebarw)


    bg_norm_show = axes[1, 1].imshow(masked_binary, cmap=colmap,extent=(0, 712.58, 0, 1125.12), interpolation='none')
    # f.colorbar(bg_norm_show, ax=axes[1, 1])
    axes[1, 1].set_title('d) Agujeros tapados')
    scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=10, fixed_units='um', frameon=False, color='w')
    axes[1,1].add_artist(scalebarw)

    plt.setp(axes[0, :], xlabel=' x [\u03BCm]')
    plt.setp(axes[0, :], ylabel='y [\u03BCm]')
    plt.show()"""

df = pd.concat(data)
df['equivalent_diameter'] = df['equivalent_diameter'] * pixels_to_microns
df['area'] = df['area'] * pixels_to_microns **2
df['convex_area']=df['convex_area']*pixels_to_microns**2
df['filled_area']=df['filled_area']*pixels_to_microns**2
df['extent'] = df['extent']*pixels_to_microns**2
df['major_axis_length'] = df['major_axis_length']*pixels_to_microns
df['minor_axis_length'] = df['minor_axis_length']*pixels_to_microns
df['perimeter'] = df['perimeter']*pixels_to_microns
df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsAZUL_df.pkl")

