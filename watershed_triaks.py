import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import measure,color,io,util,filters,feature
from skimage.measure import regionprops_table
from skimage.color import rgb2gray
from skimage.segmentation import clear_border
import pandas as pd


img1 = io.imread('C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Banda2scenes/Banda2scenes_m007.png')
img = rgb2gray(img1)
img = util.invert(img)

pixels_to_microns = 0.586

img = util.img_as_ubyte(img)
ret1,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)

opening = clear_border(opening)

sure_bg = cv2.dilate(opening,kernel,iterations=10)

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,3)
ret2,sure_fg = cv2.threshold(dist_transform,0.001*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)

unknown = cv2.subtract(sure_bg,sure_fg)
ret3,markers = cv2.connectedComponents(sure_fg)
markers += 10
markers[unknown==255] = 0

markers = cv2.watershed(img1,markers)

img1[markers==-1] = [0,255,255]
img2 = color.label2rgb(markers,bg_label=0)
f,(ax0,ax1) = plt.subplots(1,2,figsize=(10,5))
ax0.imshow(img1,cmap='gray')
ax1.imshow(img2,cmap='gray')
plt.show()


props = regionprops_table(markers,intensity_image= img,properties=['label','area','centroid','equivalent_diameter','extent'])

data = pd.DataFrame(props)
data['equivalent_diameter'] = data['equivalent_diameter']*pixels_to_microns
data['area'] = data['area']*pixels_to_microns*pixels_to_microns
print(data)