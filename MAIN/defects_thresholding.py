from skimage.filters import threshold_yen,threshold_isodata
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
proplist = ['equivalent_diameter','area']

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/norm/*.tif"

data= []
holes_data = []
i=0

for file in glob.glob(path):
    img = io.imread(file)
    img = img_as_float(img)
    thresh = threshold_yen(img)
    binary = img <= thresh
    binary_var = img <= (thresh - 0.02*thresh)
    masked_binary = ndimage.binary_fill_holes(binary)
    masked_binary_var = ndimage.binary_fill_holes(binary_var)
    hols = masked_binary.astype(int) - binary
    hols_var = masked_binary_var.astype(int) - binary_var
    lab = measure.label(hols,connectivity=2)
    lab_var = measure.label(hols_var, connectivity=2)
    cleaned_holes = morphology.remove_small_objects(lab, connectivity=2)
    cleaned_holes_var = morphology.remove_small_objects(lab_var, connectivity=2)

    label_image = measure.label(masked_binary,connectivity=2)
    label_image_var = measure.label(masked_binary_var, connectivity=2)
    label_final = morphology.remove_small_objects(label_image, min_size=500)
    label_final_var = morphology.remove_small_objects(label_image_var, min_size=500)
    if label_final.any()!=0  and label_final_var.any() !=0:
        props = regionprops_table(label_final, intensity_image=img, properties=proplist)
        props_var = regionprops_table(label_final_var, intensity_image=img, properties=proplist)
        props_df = pd.DataFrame(props)
        props_df_var = pd.DataFrame(props_var)
        props_df['error_diameter'] = abs(round((props_df['equivalent_diameter'] - props_df_var['equivalent_diameter'])*pixels_to_microns))
        props_df['error_area'] = abs(round((props_df['area'] - props_df_var['area']) * pixels_to_microns ** 2))
        props_df['img'] = i
        data.append(props_df)
        print('defects_df')
        print(props_df)
        print('error')
        print(props_df['error_diameter'])

    if cleaned_holes.any()!= 0 and cleaned_holes_var.any() != 0:
        props_holes = regionprops_table(cleaned_holes, intensity_image=img, properties=proplist)
        props_holes_var = regionprops_table(cleaned_holes_var, intensity_image=img, properties=proplist)
        holes_df = pd.DataFrame(props_holes)
        holes_df_var = pd.DataFrame(props_holes_var)
        holes_df['error_diameter'] = abs(round((holes_df['equivalent_diameter'] - holes_df_var['equivalent_diameter'])*pixels_to_microns))
        holes_df['error_area'] = abs(round((holes_df['area'] - holes_df_var['area']) * pixels_to_microns**2))
        holes_df['img'] = i
        holes_data.append(holes_df)
        print('holes_df')
        print(holes_df)
        print('error holes')
        print(holes_df['error_diameter'])
    print(file, i)
    i += 1

df = pd.concat(data)
df['equivalent_diameter'] = round(df['equivalent_diameter'] * pixels_to_microns)
df['area'] = round(df['area'] * pixels_to_microns **2)
df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsNIR_df.pkl")


holes_df = pd.concat(holes_data)
holes_df['equivalent_diameter'] = round(holes_df['equivalent_diameter'] * pixels_to_microns)
holes_df['area'] = round(holes_df['area'] * pixels_to_microns **2)
holes_df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsholesNIR_df.pkl")

