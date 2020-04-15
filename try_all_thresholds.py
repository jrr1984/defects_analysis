from skimage import filters,io,img_as_float
import matplotlib.pyplot as plt
import glob
from skimage import color, morphology

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/norm/*.tif"


for file in glob.glob(path):
    img = io.imread(file)
    img = img_as_float(img)
    selem = morphology.disk(2)
    res = morphology.white_tophat(img, selem)
    filters.try_all_threshold(img-res,figsize=(10,10),verbose=False);
    plt.show()
    # f, (ax0, ax1,ax2) = plt.subplots(1, 3, figsize=(10, 10),sharex=True,sharey=True)
    # ax0.imshow(img, cmap='gray')
    # ax1.imshow(res, cmap='gray')
    # ax2.imshow(img-res,cmap='gray')
    # plt.show()