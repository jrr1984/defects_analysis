from skimage.filters import threshold_yen
from skimage import io,measure,img_as_float,morphology
from skimage.measure import regionprops_table
from skimage.color import label2rgb
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
import pandas as pd
import glob

pixels_to_microns = 0.586
hole_thresh = 0.975
proplist = ['equivalent_diameter','perimeter','area','extent']

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Azul/norm/*.tif"

data= []
holes_data = []
i=0

for file in sorted(glob.glob(path)):
    img = io.imread(file)
    img = img_as_float(img)
    thresh = threshold_yen(img)
    binary = img <= thresh
    masked_binary =ndimage.binary_fill_holes(binary)
    # hols = masked_binary.astype(int) - binary
    label_image = measure.label(masked_binary)


    contours = measure.find_contours(img, hole_thresh)
    contour_image = np.zeros(img.shape)
    for c in contours:
        c = np.round(c).astype(int)
        coords = (c[:, 0], c[:, 1])
        contour_image[coords] = 1

    hole_binary = contour_image >= hole_thresh
    cont_img = ndimage.binary_fill_holes(hole_binary)
    cleaned_holes = morphology.remove_small_objects(cont_img, min_size=47,connectivity=8)
    hole_label = measure.label(hols)

    props = regionprops_table(label_image, intensity_image=img, properties=proplist)
    props_df = pd.DataFrame(props)
    props_df['img'] = i
    data.append(props_df)
    print('defects_df')
    print(props_df)

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
    axes[1,0].imshow(img, cmap=colmap, interpolation='none')
    axes[1, 0].set_title('b) Histograma Imagen Normalizada')
    # axes[1, 0].axvline(thresh, color='r')

    # img_norm_show = axes[0, 1].imshow(binary[510:1050,500:1150],extent=(0,316.44,0,380.9), cmap=colmap, interpolation='none')
    img_norm_show = axes[0, 1].imshow(binary, cmap=colmap, interpolation='none')
    axes[0, 1].set_title('c) Imagen Binaria')
    scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='w')
    axes[0, 1].add_artist(scalebarw)

    axes[1, 1].imshow(hols, cmap=colmap, interpolation='none')
    axes[1, 1].set_title('d) Agujeros tapados')
    scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='w')
    axes[1, 1].add_artist(scalebarw)
    axes[1, 1].set_xticks([])
    axes[1, 1].set_yticks([])
    plt.setp(axes[0, :], xlabel=' x [\u03BCm]')
    plt.setp(axes[0, :], ylabel='y [\u03BCm]')
    # plt.setp(axes[1, 1], xlabel=' x [\u03BCm]')
    # plt.setp(axes[1, 1], ylabel='y [\u03BCm]')
    plt.show()

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
df['extent'] = df['extent']*pixels_to_microns**2
df['perimeter'] = df['perimeter']*pixels_to_microns
df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsAZUL_df.pkl")

holes_df = pd.concat(holes_data)
holes_df['equivalent_diameter'] = holes_df['equivalent_diameter'] * pixels_to_microns
holes_df['area'] = holes_df['area'] * pixels_to_microns **2
holes_df['extent'] = holes_df['extent']*pixels_to_microns**2
holes_df['perimeter'] = holes_df['perimeter']*pixels_to_microns
holes_df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsholesAZUL_df.pkl")

