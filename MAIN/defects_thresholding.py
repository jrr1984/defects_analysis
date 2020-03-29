from skimage.filters import threshold_yen,threshold_otsu,threshold_triangle
from skimage import io,measure,img_as_float
from skimage.measure import regionprops_table
from skimage.color import label2rgb
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import pandas as pd
import glob

pixels_to_microns = 0.586
proplist = ['area','convex_area','filled_area','major_axis_length','minor_axis_length',
            'perimeter','equivalent_diameter','extent']

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/BandaRoja/norm/*.tif"

data= []
i=0

for file in glob.glob(path):
    img = io.imread(file)
    img = img_as_float(img)
    filters.try_all_threshold(img);
    plt.show()
    thresh = threshold_triangle(img)
    print(thresh)
    binary = img <= thresh
    masked_binary =ndimage.binary_fill_holes(binary)
    label_image = measure.label(masked_binary)


    props = regionprops_table(label_image, intensity_image=img, properties=proplist)
    props_df = pd.DataFrame(props)
    print(props_df)
    print(file,i)
    props_df['img'] = i
    i += 1
    data.append(props_df)

    image_label_overlay = label2rgb(label_image, image=img, bg_label=0)
    f, (ax0, ax1,ax2) = plt.subplots(1, 3, figsize=(10, 5),sharex=True,sharey=True)
    ax0.imshow(masked_binary, cmap='gray')
    ax1.imshow(image_label_overlay, cmap='gray')
    ax2.imshow(img, cmap='gray')
    plt.show()

df = pd.concat(data)
df['equivalent_diameter'] = df['equivalent_diameter'] * pixels_to_microns
df['area'] = df['area'] * pixels_to_microns **2
df['convex_area']=df['convex_area']*pixels_to_microns**2
df['filled_area']=df['filled_area']*pixels_to_microns**2
df['extent'] = df['extent']*pixels_to_microns**2
df['major_axis_length'] = df['major_axis_length']*pixels_to_microns
df['minor_axis_length'] = df['minor_axis_length']*pixels_to_microns
df['perimeter'] = df['perimeter']*pixels_to_microns
df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsRojo_df.pkl")

