from skimage.filters import threshold_yen, threshold_local,rank
from skimage.morphology import disk
import glob
from skimage import img_as_float,io
import matplotlib.pyplot as plt
path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/BandaRoja/norm/*.tif"


for file in glob.glob(path):
    img = io.imread(file)
    img = img_as_float(img)
    radius = 6
    selem = disk(radius)

    local_otsu = rank.otsu(img, selem)
    threshold_global_otsu = threshold_yen(img)
    global_otsu = img >= threshold_global_otsu

    fig, axes = plt.subplots(2, 2, figsize=(8, 5), sharex=True, sharey=True)
    ax = axes.ravel()
    plt.tight_layout()

    fig.colorbar(ax[0].imshow(img, cmap=plt.cm.gray),
                 ax=ax[0], orientation='horizontal')
    ax[0].set_title('Original')
    ax[0].axis('off')

    fig.colorbar(ax[1].imshow(local_otsu, cmap=plt.cm.gray),
                 ax=ax[1], orientation='horizontal')
    ax[1].set_title('Local Otsu (radius=%d)' % radius)
    ax[1].axis('off')

    ax[2].imshow(img <= local_otsu, cmap=plt.cm.gray)
    ax[2].set_title('Original >= Local Otsu' % threshold_global_otsu)
    ax[2].axis('off')

    ax[3].imshow(global_otsu, cmap=plt.cm.gray)
    ax[3].set_title('Global Otsu (threshold = %d)' % threshold_global_otsu)
    ax[3].axis('off')

    plt.show()