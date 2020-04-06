import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
import glob
from skimage import img_as_float



path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/Tiles/*.png"
bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/back_NIR.tif")
bg_mean = np.mean(bg)
bins = 1000
i=0
for file in glob.glob(path):
    i += 1
    img = io.imread(file)
    img = img_as_float(img)
    img_mean = np.mean(img)

    bg_norm = bg*img_mean
    img_norm = img*bg_mean
    diff = img_norm - bg_norm
    min_result = diff - np.min(diff)
    hist_eq = np.max(diff)-np.min(diff)
    result = min_result/hist_eq
    save_img = io.imsave("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/norm/normNIR_{}.tif".format(str(i)), result)

    # normm = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/norm/normNIR_{}.tif".format(str(i)))


"""
    #plot image process step by step comparison
    colmap = 'Greys_r'
    f, axes = plt.subplots(2, 3, figsize=(20, 20),sharex=True,sharey=True)
    img_show = axes[0,0].imshow(img,cmap=colmap,extent=(0, 712.58, 0, 1125.12), interpolation='none')
    f.colorbar(img_show, ax=axes[0,0])
    axes[0,0].set_title('a) Imagen Original')
    scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='Black')
    axes[0,0].add_artist(scalebarb)
    bg_show = axes[1,0].imshow(bg,cmap=colmap,extent=(0, 712.58, 0, 1125.12), interpolation='none')
    f.colorbar(bg_show, ax=axes[1, 0])
    axes[1, 0].set_title('b) Imagen de Fondo')
    scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='w')
    axes[1,0].add_artist(scalebarw)
    img_norm_show = axes[0, 1].imshow(img_norm, cmap=colmap,extent=(0, 712.58, 0, 1125.12), interpolation='none')
    f.colorbar(img_norm_show, ax=axes[0, 1])
    axes[0, 1].set_title('c) Imagen Original Pesada')
    scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='Black')
    axes[0,1].add_artist(scalebarb)
    bg_norm_show = axes[1, 1].imshow(bg_norm, cmap=colmap,extent=(0, 712.58, 0, 1125.12), interpolation='none')
    f.colorbar(bg_norm_show, ax=axes[1, 1])
    axes[1, 1].set_title('d) Imagen de Fondo Pesada')
    scalebarw = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='w')
    axes[1,1].add_artist(scalebarw)
    diff_show = axes[0, 2].imshow(diff, cmap=colmap,extent=(0, 712.58, 0, 1125.12), interpolation='none')
    f.colorbar(diff_show, ax=axes[0, 2])
    axes[0, 2].set_title('e) (c) - d))')
    scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='Black')
    axes[0,2].add_artist(scalebarb)
    result_show = axes[1, 2].imshow(result, cmap=colmap,extent=(0, 712.58, 0, 1125.12), interpolation='none')
    f.colorbar(result_show, ax=axes[1, 2])
    axes[1, 2].set_title('f) Imagen Final Normalizada')
    scalebarb = ScaleBar(1, 'um', location='lower right', fixed_value=50, fixed_units='um', frameon=False, color='Black')
    axes[1, 2].add_artist(scalebarb)
    plt.setp(axes[-1, :], xlabel=' x [\u03BCm]')
    plt.setp(axes[:, 0], ylabel='y [\u03BCm]')
    plt.show()
"""























