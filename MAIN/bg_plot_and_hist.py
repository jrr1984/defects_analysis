import matplotlib.pyplot as plt
from skimage import io

bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/back_NIR.tif")

f = plt.figure(1)
img_show = plt.imshow(bg, cmap='Greys_r')
f.colorbar(img_show)

bins = 500
plt.figure(2)
plt.hist(bg.ravel(), bins=bins, color='Blue', alpha=0.5)
plt.show()

