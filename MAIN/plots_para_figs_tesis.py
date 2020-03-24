import matplotlib.pyplot as plt
import glob
from skimage import io

bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/back_NIR.tif")
fig = plt.figure(figsize=(10, 10), frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(bg, cmap='Greys_r')
plt.show()
# f, (ax0, ax1,ax2,ax3) = plt.subplots(1, 4, figsize=(10, 5))
# ax0.imshow(img, cmap='gray')
# ax1.imshow(normm, cmap='gray')
# ax2.imshow(bg, cmap='gray')
# ax3.imshow(bg2, cmap='gray')
# plt.show()
