from skimage import filters,io,img_as_float
import matplotlib.pyplot as plt
import glob
from skimage import color, morphology

path = "C:/Users/juanr/Documents/mediciones_ZEISS/TILING/BandaRoja/norm/*.tif"


for file in glob.glob(path):
    img = io.imread(file)
    img = img_as_float(img)
    selem = morphology.disk(1)
    res = morphology.white_tophat(img, selem)
    filters.try_all_threshold(img-res,figsize=(10,10),verbose=True);
    plt.show()