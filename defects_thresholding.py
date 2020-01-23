from skimage.filters import threshold_yen
from skimage import io,measure
from skimage.measure import regionprops_table
from skimage.color import label2rgb


import matplotlib.pyplot as plt
import pandas as pd
import glob

pixels_to_microns = 0.586
proplist = ['area','convex_area','filled_area','major_axis_length','minor_axis_length',
            'perimeter','equivalent_diameter','extent']

path = "C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Bandanorm/*.png"
data= []
i=0

for file in glob.glob(path):
    img = io.imread(file)
    thresh = threshold_yen(img)
    binary = img <= thresh
    label_image = measure.label(binary)

    props = regionprops_table(label_image, intensity_image=img, properties=proplist)
    props_df = pd.DataFrame(props)
    print(props_df)
    props_df['img'] = i
    i += 1
    data.append(props_df)

    image_label_overlay = label2rgb(label_image, image=img,bg_label=0)
    # f, (ax0, ax1) = plt.subplots(1, 2, figsize=(10, 5))
    # ax0.imshow(binary, cmap='gray')
    # ax1.imshow(image_label_overlay, cmap='gray')
    # plt.show()

df = pd.concat(data)
df['equivalent_diameter'] = df['equivalent_diameter'] * pixels_to_microns
df['area'] = df['area'] * pixels_to_microns **2
df['convex_area']=df['convex_area']*pixels_to_microns**2
df['filled_area']=df['filled_area']*pixels_to_microns**2
df['extent'] = df['extent']*pixels_to_microns**2
df['major_axis_length'] = df['major_axis_length']*pixels_to_microns
df['minor_axis_length'] = df['minor_axis_length']*pixels_to_microns
df['perimeter'] = df['perimeter']*pixels_to_microns
df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defects_df.pkl")

