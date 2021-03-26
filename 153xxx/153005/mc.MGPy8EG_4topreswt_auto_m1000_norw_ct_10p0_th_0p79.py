# resonance mass and width
mass=1000.0
width="auto"
# process ID
# - restt: pp > resonance tt > tttt
# - resjt: pp > resonance jt > jttt
# - reswt: pp > resonance Wt > Wttt
process_id="reswt"
# resonance coupling to top quarks
ct1=10.0
#  chirality parameter
from math import pi
theta1=pi/4.
reweight = False
include("MadGraphControl_TopPhilicG_4t_v2.py")
