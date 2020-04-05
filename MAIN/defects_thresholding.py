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

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/BandaPanc/norm/*.tif"

data= []
holes_data = []
i=0

for file in glob.glob(path):
    img = io.imread(file)
    img = img_as_float(img)
    thresh = threshold_yen(img)
    binary = img <= thresh
    masked_binary =ndimage.binary_fill_holes(binary)
    hols = masked_binary.astype(int) - binary
    lab = measure.label(hols,connectivity=2)
    cleaned_holes = morphology.remove_small_objects(lab, connectivity=2)

    label_image = measure.label(masked_binary,connectivity=2)
    label_final = morphology.remove_small_objects(label_image, min_size=4000)
    if label_final.any()!=0:
        props = regionprops_table(label_final, intensity_image=img, properties=proplist)
        props_df = pd.DataFrame(props)
        props_df['img'] = i
        data.append(props_df)
        print('defects_df')
        print(props_df)

    if cleaned_holes.any() != 0:
        props_holes = regionprops_table(cleaned_holes, intensity_image=img, properties=proplist)
        holes_df = pd.DataFrame(props_holes)
        holes_df['img'] = i
        holes_data.append(holes_df)
        print('holes_df')
        print(holes_df)
    print(file, i)
    i += 1

df = pd.concat(data)
df['equivalent_diameter'] = df['equivalent_diameter'] * pixels_to_microns
df['area'] = df['area'] * pixels_to_microns **2
df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsPANC_df.pkl")

holes_df = pd.concat(holes_data)
holes_df['equivalent_diameter'] = holes_df['equivalent_diameter'] * pixels_to_microns
holes_df['area'] = holes_df['area'] * pixels_to_microns **2
holes_df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsholesPANC_df.pkl")

