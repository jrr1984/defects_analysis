from skimage.filters import threshold_yen,threshold_otsu
from skimage import io,util,measure,feature,filters
from skimage.color import label2rgb,rgb2gray
from skimage.morphology import reconstruction
from skimage.morphology import closing, square

import matplotlib.pyplot as plt
import numpy as np
import glob

path = "C:/Users/juanr/Documents/mediciones_ZEISS/bandas/Bandanorm/*.png"

for file in glob.glob(path):
    img = io.imread(file)
    thresh = threshold_yen(img)
    binary = img <= thresh
    ots_th = threshold_otsu(img)
    ots_bin = img <= thresh

    bw = closing(img > ots_th, square(3))
    seed = np.copy(img)
    seed[1:-1, 1:-1] = img.min()
    rec = reconstruction(seed, img, method='dilation')

    label_image = measure.label(bw)
    image_label_overlay = label2rgb(label_image, image=img)



    f, (ax0, ax1,ax2) = plt.subplots(1, 3, figsize=(10, 5))
    ax0.imshow(img, cmap='gray')
    ax1.imshow(rec, cmap='gray')
    ax2.imshow(ots_bin, cmap='gray')
    plt.show()