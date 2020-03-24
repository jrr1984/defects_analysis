import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import glob
from skimage import img_as_float

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/Tiles/*.png"
bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/back_NIR.tif")
bg_mean = np.mean(bg)
bins = 1000
i=0
for file in glob.glob(path):
    i+=1
    img = io.imread(file)
    img_mean = np.mean(img)

    bg_norm = bg*img_mean
    img_norm = img*bg_mean
    result = img_norm - bg_norm
    result = result - np.min(result)
    result = result/np.max(result)
    save_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/norm/normNIR_{}.tif".format(str(i)), result)


    normm = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/norm/normNIR_{}.tif".format(str(i)))
    #
    f, axes = plt.subplots(2, 2, figsize=(20, 20))
    img_show = axes[0,0].imshow(img,cmap='Blues')
    f.colorbar(img_show, ax=axes[0,0])
    normm_show = axes[0,1].imshow(normm,cmap='Blues')
    f.colorbar(normm_show, ax=axes[0, 1])
    img_float = img_as_float(img) #para comparar los histogramas en la misma escala.
    axes[1, 0].hist(img_float.ravel(), bins=bins, color='Blue', alpha=0.5)
    axes[1, 1].hist(normm.ravel(), bins=bins, color='Blue', alpha=0.5)
    plt.show()

























