import cv2
from matplotlib import pyplot as plt
from skimage import exposure,util
import pandas as pd
import numpy as np
import seaborn as sns
from pandas_profiling import ProfileReport
sns.set(color_codes=True)
plt.rcParams["font.size"] = "15"
df1 = pd.read_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsAZUL_df.pkl")
df2 = pd.read_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsVERDE_df.pkl")
df3 = pd.read_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsPANC_df.pkl")
df4 = pd.read_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsROJA_df.pkl")
df5 = pd.read_pickle("C:/Users/juanr/Documents/data_mediciones/defects/defectsNIR_df.pkl")
df = pd.concat([df1, df2, df3,df4,df5], ignore_index=True)

"""
plt.figure(1)
ax = sns.distplot(df['equivalent_diameter'],bins=70, kde=False, color='Blue',norm_hist=False)
ax.set(xlabel='Diámetro equivalente [\u03BCm]', ylabel='Número de defectos')
plt.xlim(2, 6)

plt.figure(2)
ax2 = sns.distplot(df['equivalent_diameter'],bins=70, kde=False, color='Blue',norm_hist=False)
ax2.set(xlabel='Diámetro equivalente [\u03BCm]', ylabel='Número de defectos')
plt.xlim(6, 82)

plt.figure(3)
ax3 = sns.boxplot(x='equivalent_diameter', data=df, orient="h")
ax3.set(xlabel='Diámetro equivalente [\u03BCm]')
"""

plt.figure(1)
df.plot.pie(y='equivalent_diameter')
plt.show()

