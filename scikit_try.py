import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import io,util
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops,regionprops_table
from skimage.morphology import closing, square
from skimage.color import label2rgb,rgb2gray

pixels_to_microns = 0.586
proplist = ['area','convex_area','filled_area','major_axis_length','minor_axis_length',
            'perimeter','equivalent_diameter','extent']
img = io.imread('C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Bandanorm/norm_122.png')
img = rgb2gray(img)
image = util.invert(img)

# apply threshold
thresh = threshold_otsu(image)
bw = closing(image > thresh, square(3))

# remove artifacts connected to image border


# label image regions
label_image = label(bw)
image_label_overlay = label2rgb(label_image, image=image)




props = regionprops_table(label_image, intensity_image=img, properties=proplist)
df = pd.DataFrame(props)
df['equivalent_diameter'] = df['equivalent_diameter'] * pixels_to_microns
df['area'] = df['area'] * pixels_to_microns **2
df['convex_area']=df['convex_area']*pixels_to_microns**2
df['filled_area']=df['filled_area']*pixels_to_microns**2
df['extent'] = df['extent']*pixels_to_microns**2
df['major_axis_length'] = df['major_axis_length']*pixels_to_microns
df['minor_axis_length'] = df['minor_axis_length']*pixels_to_microns
df['perimeter'] = df['perimeter']*pixels_to_microns
print(df)

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(image_label_overlay)
for region in regionprops(label_image):
    # take regions with large enough areas
    if region.area >= 10:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

ax.set_axis_off()
plt.tight_layout()
plt.show()