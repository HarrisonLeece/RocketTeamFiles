## Rocket calculations in python.
## Objective: Characterize the motion of a rocket given certain
##            values using numerical methods.
## Debugged by Matt Abel
import math
from rocketRK4 import RK4

# Inputs
# gravity, isp, atmosphere and thrust are assumed constant
# Units should be in slug for imperial and kg for metric
gravity = 32.2
mass = (600/gravity)
finalMass = (100/gravity)
isp = 290
thrust = 3000
Area = 3.1416 * 1/4 * 1
# A Supersonic fighter has a Cd of .016.  Subsonic is .012 therefore
# A rocket = .01?
Cd = .05

#Establishes mDot from thrust, gravity and isp
mDot = thrust/(gravity * isp)

#Step size of calculations.  Smaller number = higher precision
stepSize = .05
#Generally, do not change these.  Describes initial conditions and
#initializes the variables
t=0
v=0

x = 0
burnOutTime = 0
burnOutVelocity = 0
currentVelocity = 0
currentTime = 0

# Passes curren time 'step' conditions to RK4 function
# Returns the next time 'step' conditions.
# Eqaution is modified in RK4.py file

while (True):

    
    v = RK4(t,v, mass, finalMass, Cd, thrust, mDot, gravity, Area, stepSize)
    ####print('check 0')
    
    if v > 0:
        if (mass > finalMass):
            mass = mass - mDot * stepSize
            burnOutTime = t
            burnOutVelocity = v
        else:
            mass = mass
        #Computes current displacement
        x = x + ((currentVelocity + v)/2 * stepSize)
        currentVelocity = v
        #steps the while loop forward in time
        ####print('check' + str(t))
        t = t + stepSize
        print(x)
        
    else:
        break
print('Burnout at ' + str(burnOutTime))
print('Burnout velocity ' + str(burnOutVelocity) )
print(t)
print(x)

            
