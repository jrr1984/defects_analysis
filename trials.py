import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage import exposure,util

img = cv2.imread('C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Banda2norm/norm_1.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = util.img_as_ubyte(gray)
plt.imshow(gray,cmap='gray')
better_contrast = exposure.rescale_intensity(img)
v_min, v_max = np.percentile(gray, (0.2, 99.8))
better_contrast = exposure.rescale_intensity(gray, in_range=(v_min, v_max))

ret, thresh = cv2.threshold(better_contrast,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 1)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=10)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)


# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

f,(ax0,ax1) = plt.subplots(1,2,figsize=(10,5))
ax0.imshow(img,cmap='gray')
ax1.imshow(markers,cmap='gray')
plt.show()