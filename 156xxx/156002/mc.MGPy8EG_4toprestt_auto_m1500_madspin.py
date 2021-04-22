#! /usr/bin/env pythonrun
from MadGraphControl.MadGraphUtils import *
from itertools import product
from math import pi

#---------------------------------------------------------------------------------------------------                                               
# Set parameters                                                                                                                                   
#---------------------------------------------------------------------------------------------------                                               
lhe_version = 3.0

# resonance mass and width
mass=1500.0
width="auto"
# process ID
# - restt: pp > resonance tt > tttt
# - resjt: pp > resonance jt > jttt
# - reswt: pp > resonance Wt > Wttt
process_id="restt"
# resonance coupling to top quarks
ct1=1.0
#  chirality parameter
from math import pi
theta1=pi/4.

# Set defaults if parameters are not set in entry level job option
try:
  mass
except NameError:
  mass = 1500.0
  print('Warning: {parameter} not set. Setting it to default value of {default}'.format(
    parameter="resonance mass (mass)", default=mass))
try:
  width
except NameError:
  width = "auto"
  print('Warning: {parameter} not set. Setting it to default value of {default}'.format(
    parameter="resonance width (width)", default=width))
try:
  ct1
except NameError:
  ct1 = 1.0
  print('Warning: {parameter} not set. Setting it to default value of {default}'.format(
    parameter="resonance coupling to top quarks (ct1)", default=ct1))
try:
  theta1
except NameError:
  theta1 = pi / 4.
  print('Warning: {parameter} not set. Setting it to default value of {default}'.format(
    parameter="chirality parameter (theta1)", default=theta1))
try:
  process_id
except NameError:
  process_id = "restt"
  print('Warning: {parameter} not set. Setting it to default value of {default}'.format(
    parameter="Process type (process_id: restt, resjt, or reswt)", default=process_id))

print("Job option parameters:")
print("- resonance mass {p}".format(p=mass))
print("- resonance width {p}".format(p=width))
print("- resonance coupling to top quarks {p}".format(p=ct1))
print("- chirality parameter {p}".format(p=theta1))
print("- process ID {p}".format(p=process_id))


# MadGraph PDF base fragment
import MadGraphControl.MadGraphUtils
MadGraphControl.MadGraphUtils.MADGRAPH_PDFSETTING={
    # central PDF + variations for 315200 / NNPDF31_lo_as_0130
    'central_pdf':315200, # the lhapf id of the central pdf, see https://lhapdf.hepforge.org/pdfsets
    'pdf_variations':[315200], # pdfs for which all variations (error sets) will be included as weights
    'alternative_pdfs':[], # pdfs for which only the central set will be included as weights
    'scale_variations':[0.5,1.,2.], # variations of muR and muF wrt the central scale, all combinations of muF and muR will be evaluated
    # 'use_syst': "False", # use this and comment the previous ones if systematic variations are not needed
}

extras = {'auto_ptj_mjj':'False',
          'maxjetflavor':'5',
          'event_norm':'sum',
          'cut_decays':'F', 
          'dynamical_scale_choice':3,
          }

# set bwcutoff to 150 for tttt and ttttsm production to ensure that
# the resonance is written always to the LHE record
# (does not affect cross-section, as no decay chain syntax is used for these processes)
if process_id in ['tttt', 'ttttsm']:
  extras['bwcutoff'] = 150

parameters = {
    'mass':{
        'MB': 0.,
        'Mv1': mass,
    },
    'decay':{
        'Wv1': width,
    },
    'v0params': {
      'ct1': ct1,
    },
    'v1params': {
      'theta1': theta1
    }
}

# this could be changed if event multipliers were ever needed
nevents=runArgs.maxEvents
if (nevents <0):
  nevents=5000

#---------------------------------------------------------------------------------------------------                                               
# Determine MadGraph process                                                                                                                                 
#---------------------------------------------------------------------------------------------------                                               
process_string = {
 "restt": "generate p p > t t~ v1/v1, v1 > t t~",
 "resjt": "generate p p > top j v1/v1, v1 > t t~",
 "reswt": "generate p p > top w v1/v1, v1 > t t~",
 "tttt": "generate p p > t t~ t t~ QCD<=2 Qv1<=2 QED=0",
 "ttttsm": "generate p p > t t~ t t~ QCD<=4 Qv1<=2 QED=0",
}

process = """
import model Top-Philic_UFO_V1_v2
define p = g u c d s u~ c~ d~ s~ b b~
define j = g u c d s u~ c~ d~ s~ b b~
define top = t t~
define w = w+ w-
{process_string}
output -f""".format(process_string=process_string[process_id])

process_dir = new_process(process)

#---------------------------------------------------------------------------------------------------                                               
# Define run card                                                                                                                                   
#---------------------------------------------------------------------------------------------------                                               
modify_run_card(process_dir=process_dir, runArgs=runArgs, settings=extras)

#---------------------------------------------------------------------------------------------------                                               
# Define parameter card                                                                                                                             
#---------------------------------------------------------------------------------------------------                                               
modify_param_card(process_dir=process_dir, params={k:v for (k,v) in parameters.items()})

#---------------------------------------------------------------------------------------------------                                               
# Add MadSpin card
#---------------------------------------------------------------------------------------------------                
# MadSpin
bwcut = 15
topdecay = "decay t > w+ b, w+ > all all \ndecay t~ > w- b~, w- > all all \n"

madspin_card_loc=process_dir+'/Cards/madspin_card.dat'
mscard = open(madspin_card_loc,'w')
mscard.write("""#************************************************************
#*                        MadSpin                           *
#*                                                          *
#*    P. Artoisenet, R. Frederix, R. Rietkerk, O. Mattelaer *
#*                                                          *
#*    Part of the MadGraph5_aMC@NLO Framework:              *
#*    The MadGraph5_aMC@NLO Development Team - Find us at   *
#*    https://server06.fynu.ucl.ac.be/projects/madgraph     *
#*                                                          *
#************************************************************
set max_weight_ps_point 400  # number of PS to estimate the maximum for each event
set BW_cut %i
set seed %i
%s
launch
"""%(bwcut, runArgs.randomSeed, topdecay))
mscard.close()

#---------------------------------------------------------------------------------------------------                                               
# Check cards and proceed with event generation                                                                                                                             
#---------------------------------------------------------------------------------------------------   
print_cards()
generate(process_dir=process_dir, runArgs=runArgs)
arrange_output(process_dir=process_dir, runArgs=runArgs, lhe_version=lhe_version)

#---------------------------------------------------------------------------------------------------                                               
# Storing information and post-processing with parton shower                                                                                                                            
#---------------------------------------------------------------------------------------------------   
# Some more information
evgenConfig.description = "pp -> ttV1, V1->tt signal point"
evgenConfig.keywords = ["exotic", "BSM", "RandallSundrum", "warpedED"]
evgenConfig.contact = ["James Ferrando <james.ferrando@desy.de>", "Philipp Gadow <paul.philipp.gadow@cern.ch>"]
evgenConfig.process = "pp>ttv1> tttt"  # e.g. pp>G*>WW>qqqq

# Finally, run the parton shower...
include("Pythia8_i/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")

# ...and pull in MadGraph-specific stuff
include("Pythia8_i/Pythia8_MadGraph.py")
