from skimage import exposure,img_as_float
import matplotlib.pyplot as plt
import seaborn as sns

def plot_img_and_hist(image, axes, bins=65536):
    image = img_as_float(image)
    ax_img, ax_hist = axes
    # ax_cdf = ax_hist.twinx()

    # Display image
    ax_img.imshow(image, cmap=plt.cm.gray)
    ax_img.set_axis_off()

    # Display histogram

    plt.hist(image.ravel(), bins=bins, color='Blue',alpha=0.5)
    ax_hist.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    ax_hist.set_xlabel('Pixel intensity')
    ax_hist.set_xlim(0, 1)
    ax_hist.set_yticks([])
    return ax_img, ax_hist