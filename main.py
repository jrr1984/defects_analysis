import czifile
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib_scalebar.scalebar import ScaleBar
import cv2

def normalize(arr):
    arr_min = arr.min()
    arr_max = arr.max()
    return (arr - arr_min) / (arr_max - arr_min)

# img = czifile.imread('C:/Users/juanr/Documents/mediciones_ZEISS/15x15/15x15-Stitching.czi')
# img = img[0,0,0,:,:,0]
#1 canal= monocromatico, 27054 filas x 26811 columnas = (x,y)
img = cv2.imread('C:/Users/juanr/Documents/mediciones_ZEISS/15x15/15x15tiffscalebar.tif')
# img = normalize(img)
img = img[100:26700,100:26600,:]

plt.figure()
# plt.imshow(img,cmap='gray',aspect='equal',extent=(0,15711.25,0,15853.64))
plt.imshow(img,cmap='gray',aspect='equal',extent=(0,15000,0,15000))
# scalebar = ScaleBar(0.586,'um',location='lower right') # 1 pixel = 0.586 microns = 5.86 . 10^-7
# plt.gca().add_artist(scalebar)
plt.show()
