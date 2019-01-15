#Pressure Vessle calculations for Gas-Pressurized propellant feed system
#
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
#Required tank ullage
ullage = 1000
#Required propellant volumes
volF = weightF/rhoF + ullage
volO = weightO/rhoO + ullage

#Specifications of Propellant Feed System
#
tankPresPsi = 550
tankPres = tankPresPsi * 144
#Pressurant enterance temperature on rankine scale
antTemp = 460
#Volume of expelled pressurant

#Required pressurant weight
antW = 0

print('Volume of Fuel required: ' +str(volF) + ' cubic inches, after ullage requirements')
print('Volume of Oxidizer required: ' + str(volO) + ' cubic inches, after ullage requirements')
