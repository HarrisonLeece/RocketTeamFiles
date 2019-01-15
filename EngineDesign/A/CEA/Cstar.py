from rocketcea.cea_obj import CEA_Obj
from pylab import *

pcL = [ 600., 500., 300.]

ispObj = CEA_Obj(propName='', oxName='LOX', fuelName="RP1")

for Pc in pcL:
    cstarArr = []
    MR = 2.0
    mrArr = []
    while MR < 3.0:
        cstarArr.append( ispObj.get_Cstar( Pc=Pc, MR=MR) )
        mrArr.append(MR)
        MR += 0.05
    plot(mrArr, cstarArr, label='Pc=%g psia'%Pc)

legend(loc='best')
grid(True)
title( ispObj.desc )
xlabel( 'Mixture Ratio' )
ylabel( 'Cstar (ft/sec)' )
savefig('cea_cstar_plot.png', dpi=120)

show()
