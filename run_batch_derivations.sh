#!bin/bash

# Job submission for DESY HTCondor - copy to project directory and adapt to your needs
JOBNAME="TRUTH1_bsm4tops"
# DSIDS="150000 150017" #Range of DSIDs in job option directory
DSIDS="151000 151001 151002 151003 151004 151005 151006 151007 151008 151009 151010 151011 151012 151013 151014 151015 \
       152000 152001 152002 152003 \
       153000 153001 153002 153003 \
       154000 154001 154002 154003 154004 154005 154006 154007 154008 154009 154010 154011 154012 154013 154014 154015" #DSIDs in job option directory
RUNTIME="03:00:00"         #Run time per job HH:MM:SS
MEMORY=2000                #Memory per job in MB
MODELSDIR=$PWD/models

cd batch_submission
COMMAND="python SubmitMC/python/submit_derivation.py --jobName ${JOBNAME} --engine HTCONDOR -r ${DSIDS} --noBuildJob --accountinggroup af-atlas --deriv_runtime ${RUNTIME} --deriv_memory ${MEMORY}"
echo $COMMAND
$COMMAND
