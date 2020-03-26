import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y = np.array([1,1,2,8,9,12,17,19,21,31,34,45,56,65,78,97,128,158,225,266,301])
x = np.array(range(len(y)))
plt.plot(x, y,'*b')
plt.show()
popt, pcov = curve_fit(lambda t,a,b: a*np.exp(b*t),  x,  y)
