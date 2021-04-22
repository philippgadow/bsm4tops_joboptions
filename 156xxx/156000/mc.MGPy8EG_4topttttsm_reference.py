#! /usr/bin/env pythonrun
from MadGraphControl.MadGraphUtils import *
from itertools import product


#---------------------------------------------------------------------------------------------------                                               
# Set parameters                                                                                                                                   
#---------------------------------------------------------------------------------------------------                                               
lhe_version = 3.0

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

# set bwcutoff to 100 for tttt and ttttsm production to ensure that
# the resonance is written always to the LHE record
# (does not affect cross-section, as no decay chain syntax is used for these processes)
extras['bwcutoff'] = 100

parameters = {}

# this could be changed if event multipliers were ever needed
nevents=runArgs.maxEvents
if (nevents <0):
  nevents=5000

#---------------------------------------------------------------------------------------------------                                               
# Define MadGraph process                                                                                                                                 
#---------------------------------------------------------------------------------------------------                                               


process = """
define p = g u c d s u~ c~ d~ s~ b b~
define j = g u c d s u~ c~ d~ s~ b b~
define top = t t~
define w = w+ w-
generate p p > t t~ t t~ QCD<=4 QED=0
output -f"""

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
# Check cards and proceed with event generation                                                                                                                             
#---------------------------------------------------------------------------------------------------   
print_cards()
generate(process_dir=process_dir, runArgs=runArgs)
arrange_output(process_dir=process_dir, runArgs=runArgs, lhe_version=lhe_version)

#---------------------------------------------------------------------------------------------------                                               
# Storing information and post-processing with parton shower                                                                                                                            
#---------------------------------------------------------------------------------------------------   
# Some more information
evgenConfig.description = "pp -> tttt reference process"
evgenConfig.keywords = ["SM"]
evgenConfig.contact = ["Philipp Gadow <paul.philipp.gadow@cern.ch>"]
evgenConfig.process = "pp> tttt"  # e.g. pp>G*>WW>qqqq

# Finally, run the parton shower...
include("Pythia8_i/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")

# ...and pull in MadGraph-specific stuff
include("Pythia8_i/Pythia8_MadGraph.py")
