from skimage import io,util,measure,feature,filters,morphology,segmentation,color
from scipy.ndimage import distance_transform_edt
from skimage.measure import regionprops_table
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

pixels_to_microns = 0.586
proplist = ['area','convex_area','filled_area','major_axis_length','minor_axis_length',
            'perimeter','equivalent_diameter','extent']

path = "C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Bandanorm/*.png"

i=0
data = []

for file in glob.glob(path):
    img = io.imread(file)
    #img = grey2rgb(img)
    img = util.invert(img)
    #img = util.img_as_ubyte(img)
        #denoise img
    img_denoised = filters.median(img,selem=np.ones((5,5)))

    #look for edges of defects
    edges = feature.canny(img_denoised,sigma=1)

    #we already got the landscape, now let-s fill it with water
    #we put fountains inside each defect
    #euclidean distance transform: distance to the closest background pixel
    #~ inverse to the edges, we make the fg, bg and the bg, fg

    dt = distance_transform_edt(~edges)

    #we look for the location of the fountains
    local_max = feature.peak_local_max(dt,indices=False,min_distance=3)
    markers = measure.label(local_max)
    labels = morphology.watershed(-dt,markers)

    regions = measure.regionprops(labels,intensity_image=img)
    region_means = [r.mean_intensity for r in regions]
    # plt.hist(region_means,bins=100)
    # plt.show()
    model = KMeans(n_clusters=2)
    region_means = np.array(region_means).reshape(-1,1)
    model.fit(np.array(region_means))
    bg_fg_labels = model.predict(region_means)
    classified_labels = labels.copy()
    for bg_fg,region in zip(bg_fg_labels,regions):
        classified_labels[tuple(region.coords.T)] = bg_fg

    props = regionprops_table(classified_labels, intensity_image=img, properties=proplist)
    props_df = pd.DataFrame(props)
    print(props_df)
    props_df['img'] = i
    i += 1
    data.append(props_df)

    img[markers == -1] = [0]
    img1 = color.label2rgb(classified_labels, bg_label=0)
    f, (ax0, ax1) = plt.subplots(1, 2, figsize=(10, 5))
    ax0.imshow(img, cmap='gray')
    ax1.imshow(img1, cmap='gray')
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
df.to_pickle("C:/Users/juanr/Documents/defects_df.pkl")