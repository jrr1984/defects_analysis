import czifile
from skimage import io,feature,filters
import matplotlib.pyplot as plt
import numpy as np

img = czifile.imread('C:/Users/juanr/Documents/mediciones_ZEISS/15x15-Stitching.czi')
img = img[0,0,0,:,:,0]
#1 canal= monocromatico, 27054 filas x 26811 columnas = (x,y)

def normalize(arr):
    arr_min = arr.min()
    arr_max = arr.max()
    return (arr - arr_min) / (arr_max - arr_min)

img = normalize(img)

import matplotlib.cbook as cbook
from matplotlib_scalebar.scalebar import ScaleBar
plt.figure()
plt.imshow(img,cmap='gray',aspect='equal',extent=(0,15711.25,0,15853.64))
scalebar = ScaleBar(4.4e-7) # 1 pixel = 0.440 microns = 4.4 . 10^-7
plt.gca().add_artist(scalebar)
plt.show()
