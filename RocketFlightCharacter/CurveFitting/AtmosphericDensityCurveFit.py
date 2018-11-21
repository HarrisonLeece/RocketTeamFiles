## Atmospheric density curve fit from Engineering Toolbox US standard Atmosphere
## Design by Harrison Leece

from scipy import optimize
import math
import numpy as np
import matplotlib.pyplot as plt

e = math.exp(1)

def fxn(x, a, b, c):
    return a *((e**(- b * x - c)))

altitudes = np.array([0,5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,60000,70000,80000,90000,100000,150000,200000,250000])
wholeDomain = np.linspace(0,500000,500000)
density1 = np.array([23.8,20.48,17.56,14.96,12.67,10.66,8.91,7.38,5.87,4.62,3.64,2.26,1.39,.86,.56,.33,.037,.0053,.00065])

print(np.size(altitudes))
print(np.size(density1))

popt, pcov = optimize.curve_fit(fxn, altitudes, density1)

print(popt)

print(popt[0])

#Plots data
plt.grid(True)
plt.ylim((0,25))
plt.plot(altitudes, density1)
plt.plot(wholeDomain, fxn(wholeDomain, popt[0], popt[1], popt[2]))
plt.show()


