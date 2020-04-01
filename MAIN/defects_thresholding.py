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

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/BandaPanc/norm/*.tif"

data= []
holes_data = []
i=0

for file in glob.glob(path):
    img = io.imread(file)
    img = img_as_float(img)
    thresh = threshold_yen(img)
    binary = img <= thresh
    masked_binary =ndimage.binary_fill_holes(binary,structure=np.ones((5,5)))
    hols = masked_binary.astype(int) - binary
    label_image = measure.label(masked_binary)


    contours = measure.find_contours(img, hole_thresh)
    contour_image = np.zeros(img.shape)
    for c in contours:
        c = np.round(c).astype(int)
        coords = (c[:, 0], c[:, 1])
        contour_image[coords] = 1

    hole_binary = contour_image >= hole_thresh
    cont_img = ndimage.binary_fill_holes(hole_binary)
    lab = measure.label(hols)
    cleaned_holes = morphology.remove_small_objects(lab, min_size=47, connectivity=8)
    hole_label = measure.label(cleaned_holes)

    props = regionprops_table(label_image, intensity_image=img, properties=proplist)
    props_df = pd.DataFrame(props)
    props_df['img'] = i
    data.append(props_df)
    print('defects_df')
    print(props_df)

    if hole_label.any() != 0:
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
df['extent'] = df['extent']*pixels_to_microns**2
df['perimeter'] = df['perimeter']*pixels_to_microns
df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsPANC_df.pkl")

holes_df = pd.concat(holes_data)
holes_df['equivalent_diameter'] = holes_df['equivalent_diameter'] * pixels_to_microns
holes_df['area'] = holes_df['area'] * pixels_to_microns **2
holes_df['extent'] = holes_df['extent']*pixels_to_microns**2
holes_df['perimeter'] = holes_df['perimeter']*pixels_to_microns
holes_df.to_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsholesPANC_df.pkl")

