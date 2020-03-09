import cv2 as cv2
import numpy as np
from skimage import exposure,util,io,img_as_float
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import glob

# path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/Tiles/*.png"
path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/Celeste/*.png"
bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/bandas/back.tif")
bg_mean = np.mean(bg)

i=0

def plot_img_and_hist(image, axes, bins=256):
    """Plot an image along with its histogram and cumulative histogram.

    """
    image = img_as_float(image)
    ax_img, ax_hist = axes
    ax_cdf = ax_hist.twinx()

    # Display image
    ax_img.imshow(image, cmap=plt.cm.gray)
    ax_img.set_axis_off()

    # Display histogram
    ax_hist.hist(image.ravel(), bins=bins, histtype='step', color='black')
    ax_hist.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    ax_hist.set_xlabel('Pixel intensity')
    ax_hist.set_xlim(0, 1)
    ax_hist.set_yticks([])

    # Display cumulative distribution
    img_cdf, bins = exposure.cumulative_distribution(image, bins)
    ax_cdf.plot(bins, img_cdf, 'r')
    ax_cdf.set_yticks([])

    return ax_img, ax_hist, ax_cdf




for file in glob.glob(path):
    i+=1
    img = io.imread(file)
    img_mean = np.mean(img)

    bg_norm = bg*img_mean
    img_norm = img*bg_mean
    result = img_norm - bg_norm
    result = result - np.min(result)
    result = result/np.max(result)
    save_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/norm_cel/normCel_{}.tif".format(str(i)), result)


    # normm = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/Celeste/norm_cel/normCel_{}.tif".format(str(i)))
    # fig = plt.figure(figsize=(10, 7))
    # axes = np.zeros((2, 3), dtype=np.object)
    # axes[0, 0] = plt.subplot(2, 3, 1)
    # axes[0, 1] = plt.subplot(2, 3, 2, sharex=axes[0, 0], sharey=axes[0, 0])
    # axes[0, 2] = plt.subplot(2, 3, 3, sharex=axes[0, 0], sharey=axes[0, 0])
    # axes[1, 0] = plt.subplot(2, 3, 4)
    # axes[1, 1] = plt.subplot(2, 3, 5)
    # axes[1, 2] = plt.subplot(2, 3, 6)
    # ax_img, ax_hist, ax_cdf = plot_img_and_hist(img, axes[:, 0])
    # ax_img.set_title('Imagen Original')
    #
    # y_min, y_max = ax_hist.get_ylim()
    # ax_hist.set_ylabel('Número de píxeles')
    # ax_hist.set_yticks(np.linspace(0, y_max, 5))
    #
    # ax_img, ax_hist, ax_cdf = plot_img_and_hist(normm, axes[:, 1],bins=10000)
    # ax_img.set_title('Imagen Corregida')
    #
    # ax_img, ax_hist, ax_cdf = plot_img_and_hist((img-normm), axes[:, 2])
    # ax_img.set_title('Diferencia')
    #
    # ax_cdf.set_ylabel('Fracción de la Intensidad Total')
    # ax_cdf.set_yticks(np.linspace(0, 1, 5))
    #
    # fig.tight_layout()
    # plt.show()











#columnas de pixeles
#perfil de intensidad de esa columna
#[:,0] en funcion del pixel







    # f, (ax0, ax1,ax2,ax3) = plt.subplots(1, 4, figsize=(10, 5))
    # ax0.imshow(img, cmap='gray')
    # ax1.imshow(normm, cmap='gray')
    # ax2.imshow(bg, cmap='gray')
    # ax3.imshow(bg2, cmap='gray')
    # plt.show()







