from ptankObj import pTank
from ptankObj import cin_cft
import numpy as np
import plotly.graph_objs as go
import plotly.plotly as py
import plotly.tools as tls
import matplotlib.pyplot as plt


dia_range = np.linspace(6,10,9)
t_range = np.linspace(.05, .2, 11)

result = []


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
ullage = 500
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

idVect = []
tVect = []

for iD in dia_range:
    for t in t_range:
        rp1 = pTank('fuel', volF, ullage, 825, iD)
        lox = pTank('ox', volO, ullage, 825, iD)
        idVect = np.append(idVect, iD)
        tVect = np.append(tVect, t)
        result = np.append(result, rp1.hoopTee()/t)

trace1 = go.Carpet(
    a = idVect,
    b = tVect,
    y = result,
    aaxis = dict(
        
        tickprefix = 'a = ',
        ticksuffix = 'diameter, inch',
        smoothing = 1,
        minorgridcount = 9,
    ),
    baxis = dict(
        tickprefix = 'b = ',
        ticksuffix = 'thickness, inch',
        smoothing = 1,
        minorgridcount = 9,
    )
)

layout = go.Layout(
    yaxis=dict(
        type='log',
        autorange=True,
        title='Required material strength, psi',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

data = [trace1]

fig = go.Figure(data = data, layout = layout)
py.plot(fig, filename = "id_Thickness_Carpet")
