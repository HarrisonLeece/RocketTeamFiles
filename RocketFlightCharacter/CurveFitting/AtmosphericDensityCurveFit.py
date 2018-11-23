## Atmospheric density curve fit from Engineering Toolbox US standard Atmosphere
## Design by Harrison Leece

from scipy import optimize
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt



def fxn(x, a, b):
    return a*np.exp(-b*x)
def polyFxn(h, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    return  ((((((((a9*h + a8)*h + a7)*h + a6)*h + a5)*h + a4)*h + a3)*h + a2)*h + a1)*h + a0

#From Engineeringtoolbox US standard Atmosphere
altitudes = np.array([-5000,0,5000,10000,15000,20000,25000,30000,35000,40000,40001,45000,45001,50000,60000,70000,80000,90000,100000,150000,200000,250000])
density1 = np.array([27.45,23.77,20.48,17.56,14.96,12.67,10.66,8.91,7.38,5.87,5.87,4.62,4.62,3.64,2.26,1.39,.86,.56,.33,.037,.0053,.00065])

#Adds weights to help curve fit
weightedAltitudes = np.array([-5000,0,10,5000,10000,15000,15001,20000,25000,30000,35000,40000,45000,50000,60000,70000,80000,90000,100000,150000,200000,250000])
weightedDensity = np.array([27.45,23.8,23.79,20.48,17.56,14.96,14.95,12.67,10.66,8.91,7.38,5.87,4.62,3.64,2.26,1.39,.86,.56,.33,.037,.0053,.00065])

altitudeLinSpace = np.linspace(0,500000,500000)

#Popt returns a array containing constants a,b,c... etc for function 'fxn'
popt, pcov = optimize.curve_fit(fxn, weightedAltitudes, weightedDensity, p0=(1, 1e-5))
popt2, pcov2 = optimize.curve_fit(polyFxn, altitudes, density1)

print(popt)
print(popt2)


#statistics
residuals = weightedDensity - fxn(weightedAltitudes, popt[0], popt[1])
ss_res = np.sum(residuals**2)
ss_tot = np.sum((weightedDensity - np.mean(weightedDensity))**2)
r_squared = 1 - (ss_res / ss_tot)
print('R^2 = ' + str(r_squared))

#Plots data
plt.grid(True)
plt.ylim((0,25))
plt.ylabel('Density of atmospher in slug/ft^3 * 10^-4')
plt.xlabel('Altitude, feet')
#Data from engineering toolbox
plt.plot(altitudes, density1)
#curve_fit for negative exponential
plt.plot(altitudeLinSpace, fxn(altitudeLinSpace, popt[0], popt[1]))
#curve_fit for polynomial
plt.plot(altitudeLinSpace, polyFxn(altitudeLinSpace, popt2[0],popt2[1],popt2[2],popt2[3],popt2[4],popt2[5],popt2[6],popt2[7],popt2[8],popt2[9]))
plt.show()


