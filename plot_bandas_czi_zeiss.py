import czifile
from skimage import io,feature,filters
import matplotlib.pyplot as plt
import numpy as np

img = czifile.imread('C:/Users/juanr/Documents/mediciones_ZEISS/TILING/AZUL/Azul.czi')
print(img.shape)
#1 canal= monocromatico, 27054 filas x 26811 columnas = (x,y)
img = img[0,0,:,:,0]
print(img.shape)

fig = plt.figure()
bg_show = plt.imshow(img, cmap='Greys_r',extent=(0,img.shape[1]*0.586,0,img.shape[0]*0.586), interpolation='none')
plt.xlabel(' x [\u03BCm]')
plt.ylabel('y [\u03BCm]')
plt.title('Banda Azul')
plt.show()