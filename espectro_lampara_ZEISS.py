import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
wavel_df = pd.read_pickle("wavel_df.pkl")
wavel_df = wavel_df.iloc[1:]
light_df = pd.read_csv("espectro_lampZEISS.csv")

def normalize(arr):
    arr_min = arr.min()
    arr_max = arr.max()
    return (arr - arr_min) / (arr_max - arr_min)

light_df = np.array(light_df)
light_df = normalize(light_df)
light_df = light_df.transpose()
light_df= light_df[0,:]

from scipy.signal import savgol_filter
yhat = savgol_filter(light_df, 51, 3)
wavel_df = wavel_df[0:3600]
yhat = yhat[0:3600]
plt.xlabel('Longitud de onda [nm]',fontsize=28)
plt.ylabel('Intensidad [u.a.]',fontsize=28)
plt.plot(wavel_df,yhat,'*')
plt.show()
