#Temperature of atmosphere in kelvin
#Harrison Leece

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

alt = np.array([0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,15000,20000,25000,30000,40000,50000,60000,70000,80000])
#temp in degrees C
temp = np.array([15,8.5,2,-4.49,-10.98,-17.47,-23.96,-30.45,-36.94,-43.42,-49.90,-56.50,-56.50,-51.60,-46.64,-22.80,-2.5,-26.13,-53.57,-74.51])

altl_1 = np.linspace(0,20000,20000)
altl_2 = np.linspace(10000,50000,40000)
altl_3 = np.linspace(50000,100000,50000)

#portion 1
alt1 = np.array([0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,15000,20000])
t1 = np.array([15,8.5,2,-4.49,-10.98,-17.47,-23.96,-30.45,-36.94,-43.42,-49.90,-56.50,-56.50])
cof1 = np.polyfit(alt1,t1,2)
#portion 2
alt2 = np.array([15000,20000,25000,30000,40000,50000])
t2 = np.array([-56.50,-56.50,-51.60,-46.64,-22.80,-2.5])
cof2 = np.polyfit(alt2,t2,2)
#portion 3
alt3 = np.array([50000,60000,70000,80000])
t3 = np.array([-2.5,-26.13,-53.57,-74.51])
cof3 = np.polyfit(alt3,t3,1)
#Raw data plot
plt.plot(alt,temp)
plt.ylabel('Temperature')
plt.xlabel('Altitude')

#p1
plt.plot(altl_1, cof1[0]*altl_1**2 + cof1[1]*altl_1 + cof1[2])
#p2
plt.plot(altl_2, cof2[0]*altl_2**2 + cof2[1]*altl_2 + cof2[2])
#p3
plt.plot(altl_3, cof3[0]*altl_3 + cof3[1])

plt.show()

print('Phase 1 coefficients: ' + str(cof1))
print('Phase 2 coefficients: ' + str(cof2))
print('Phase 3 coefficients: ' + str(cof3))
