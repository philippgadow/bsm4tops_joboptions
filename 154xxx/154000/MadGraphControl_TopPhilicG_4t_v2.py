#! /usr/bin/env pythonrun
from MadGraphControl.MadGraphUtils import *
from itertools import product
from math import pi

#---------------------------------------------------------------------------------------------------                                               
# Set parameters                                                                                                                                   
#---------------------------------------------------------------------------------------------------                                               
lhe_version = 3.0

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

try:
  reweight
except NameError:
  reweight = True
  print('Warning: {parameter} not set. Setting it to default value of {default}'.format(
    parameter="Reweighting enabled flag", default=reweight))

print("Job option parameters:")
print("- resonance mass {p}".format(p=mass))
print("- resonance width {p}".format(p=width))
print("- resonance coupling to top quarks {p}".format(p=ct1))
print("- chirality parameter {p}".format(p=theta1))
print("- process ID {p}".format(p=process_id))
print("- ME reweighting enabled {p}".format(p=reweight))


# MadGraph PDF base fragment
import MadGraphControl.MadGraphUtils
MadGraphControl.MadGraphUtils.MADGRAPH_PDFSETTING={
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
 "restt": "generate p p > t t~ t t~ QCD<=2 Qv1=2 QED=0",
 "resjt": "generate p p > t t~ top j QCD<=2 Qv1=2 QED=0",
 "reswt": "generate p p > generate p p > t t~ top w QCD<=2 Qv1=2 QED=0",
}

process = """
import model Top-Philic_UFO_V1_v2
set zerowidth_tchannel False
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
# Add reweight card, therefore allowing for scans of theta1 and ct1
#---------------------------------------------------------------------------------------------------                
if reweight:
  ct1_scan = [0.5, 1.0, 2.5, 5.0, 7.5, 10.0, 20.0, 50.0]
  theta1_scan = [0., 1./8.*pi, 2./8.*pi, 3./8.*pi, 4./8.*pi, 5./8.*pi, 6./8.*pi, 7./8.*pi, pi]

  reweightCommand=""
  for i_ct1, i_theta1 in product(ct1_scan, theta1_scan):
    reweightCommand += "launch --rwgt_name=rwgt_ct1_{ct1_str}_theta1_{theta1_str}\n".format(
      ct1_str=str(i_ct1).replace('.', 'p'), theta1_str="{0:.2f}".format(i_theta1).replace('.', 'p')
    )
    reweightCommand += "set v0params 1 {ct1}\n".format(ct1=i_ct1)
    reweightCommand += "set v1params 1 {theta1}\n\n".format(theta1=i_theta1)

  rcard = open(os.path.join(process_dir,'Cards', 'reweight_card.dat'), 'w')
  rcard.write(reweightCommand)
  rcard.close()

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
evgenConfig.inputfilecheck = ""
evgenConfig.description = "pp -> ttV1, V1->tt signal point"
evgenConfig.keywords = ["exotic", "BSM", "RandallSundrum", "warpedED"]
evgenConfig.contact = ["James Ferrando <james.ferrando@desy.de>", "Philipp Gadow <paul.philipp.gadow@cern.ch>"]
evgenConfig.process = "pp>ttv1> tttt"  # e.g. pp>G*>WW>qqqq

# Finally, run the parton shower...
include("Pythia8_i/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")

# ...and pull in MadGraph-specific stuff
include("Pythia8_i/Pythia8_MadGraph.py")
