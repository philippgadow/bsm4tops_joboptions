# resonance mass and width
mass=2000.0
width="auto"
# process ID
# - restt: pp > resonance tt > tttt
# - resjt: pp > resonance jt > jttt
# - reswt: pp > resonance Wt > Wttt
process_id="reswt"
# resonance coupling to top quarks
ct1=1.0
#  chirality parameter
from math import pi
theta1=pi/4.
include("MadGraphControl_TopPhilicG_4t_v2.py")
