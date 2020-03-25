import matplotlib.pyplot as plt
import glob
from skimage import io
plt.rcParams["font.size"] = "15"
# bg = io.imread("C:/Users/juanr/Documents/mediciones_ZEISS/TILING/NIR/back_NIR.tif")
bg = io.imread("C:/Users/juanr/Documents/master_thesis_scratch_and_dig/tesis_tex/Figs/defectosZEISS/img_ideal_2defectos.png")
fig = plt.figure(figsize=(10, 10), frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
plt.imshow(bg, cmap='Greys_r')
# bins = 500
plt.figure(2)
# plt.hist(bg.ravel(), bins=bins, color='Blue', alpha=0.5)
plt.hist(bg.ravel(), color='Blue', alpha=0.5,log=True)
plt.xlabel(' Intensidad [u.a.]')
plt.ylabel('Número de píxeles')
# plt.xlim(0,1)
plt.show()