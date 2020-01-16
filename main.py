import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import skimage

def normalize(arr):
    arr_min = arr.min()
    arr_max = arr.max()
    return (arr - arr_min) / (arr_max - arr_min)