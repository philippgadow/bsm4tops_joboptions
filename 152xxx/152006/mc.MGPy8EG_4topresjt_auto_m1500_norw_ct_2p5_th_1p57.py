# resonance mass and width
mass=1500.0
width="auto"
# process ID
# - restt: pp > resonance tt > tttt
# - resjt: pp > resonance jt > jttt
# - reswt: pp > resonance Wt > Wttt
process_id="resjt"
# resonance coupling to top quarks
ct1=2.5
#  chirality parameter
from math import pi
theta1=pi/2.
reweight = False
include("MadGraphControl_TopPhilicG_4t_v2.py")
