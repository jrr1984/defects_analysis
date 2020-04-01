import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
a = np.zeros((10, 10), dtype=int)
a[3:7,3:7] = 1
a[4:6,4:6] = 0
print('Agujero')
print(a)

f, (ax1,ax2) = plt.subplots(1, 2, figsize=(20, 20))
f.subplots_adjust(hspace=0.4)
ax1.imshow(a,cmap='gray')
print('Agujero Tapado')
atap = ndimage.binary_fill_holes(a,structure=np.ones((3,3))).astype(int)
print(atap)
ax2.imshow(atap,cmap='gray')
plt.show()
