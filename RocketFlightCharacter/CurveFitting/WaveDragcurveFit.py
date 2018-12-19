##Harrison Leece, 
##wave drag curve fit

from scipy import optimize
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt





#Plots data
plt.grid(True)
plt.ylim((0,4))
plt.ylabel('coefficient of drag')
plt.xlabel('Mach number')

#Mercury-Atlas Cd data
plt.plot(altitudes, density1)
#curve fit
plt.plot(altitudeLinSpace, output)

plt.show()
