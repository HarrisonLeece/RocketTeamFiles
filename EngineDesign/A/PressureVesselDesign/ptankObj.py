class pTank:
    def __init__(self,catagory,propellantVol,ullageVol,pressure, innerDia):
        self.cat = catagory
        self.pVol = propellantVol
        self.ull = ullageVol
        self.pres = pressure
        self.iD = innerDia
        self.ir = innerDia/2
        self.totVol = self.pVol + self.ull 
    def hoopTee(self):
        hoopTee = self.ir * self.pres
        return hoopTee
    #result in inches
    def tankHeight(self):
        cylH = (self.totVol - 1/6 * 3.1416 * (self.iD)**3)*4/(3.1416 * (self.iD)**2)
        h = cylH + self.iD
        return h

#Test for pTank obj

def cin_cft(inches):
    return inches/(12**3)

#Pressure Vessle calculations for Gas-Pressurized propellant feed system
#Specifications of Rocket
RocketWeight = 700
propellantMassRatio = .70
pWeight = RocketWeight * propellantMassRatio
pMass = pWeight/32.2
#Engine specifications, LOX/RP1 by mass, ratio = O/F, this should be fuel rich
mr = 2.25

#Mass and weight of each proellant
massF = pMass/(mr+1)
massO = mr*pMass/(mr+1)

weightF = pWeight/(mr+1)
weightO = mr*pWeight/(mr+1)

#Density of LOx and kerosene, lbs/in^3
rhoF = .0296
rhoO = .04141
#Required tank ullage, inch^3
ullage = 1000
#Required propellant tank volumes
volF = weightF/rhoF 
volO = weightO/rhoO 
#Pressure of Propellant Feed System lbs/ft^2
tankPresPsi = 550
tankPres = tankPresPsi * 144
#Pressurant enterance temperature on rankine scale
antTemp = 460 + 30
#Volume of expelled propellants cubic feet
totVol = cin_cft(volF+volO)
#Pressurant gas constant (helium) ft-lb/(lb-R)
gasR = 386.047
#Required pressurant weight, lbs
antW = tankPres * totVol / ( gasR * antTemp )

print('Volume of Fuel required: ' +str(volF) + ' cubic inches')
print('Volume of Oxidizer required: ' + str(volO) + ' cubic inches')

iD = 7

rp1 = pTank('fuel', volF, ullage, 825, iD)
lox = pTank('ox', volO, ullage, 825, iD)
print('Combined tank height requirement: ' + str(rp1.tankHeight() + lox.tankHeight()) + ' inches')
