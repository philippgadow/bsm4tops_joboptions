#!bin/bash

# Job submission for DESY HTCondor - copy to project directory and adapt to your needs
JOBNAME="EVGEN_bsm4tops_tchan"
# DSIDS="152000 152001 152002 152003 152004 152005 152006 152007 \
#        153000 153001 153002 153003 153004 153005 153006 153007" #DSIDs in job option directory
# DSIDS="151010 151011 151012 151013 151014 151015 151016 151017" #DSIDs in job option directory
DSIDS="154000 154001 154002 154003" #DSIDs in job option directory
EVENTS=10000               #Events per job
NJOBS=1                    #Number of jobs per DSID
RUNTIME="03:00:00"         #Run time per job HH:MM:SS
MEMORY=2000                #Memory per job in MB
MODELSDIR=$PWD/models

cd batch_submission
COMMAND="python SubmitMC/python/submit.py --jobName ${JOBNAME} --engine HTCONDOR --eventsPerJob ${EVENTS} --nJobs ${NJOBS} -r ${DSIDS} --noBuildJob --modelsDir ${MODELSDIR} --accountinggroup af-atlas --evgen_runtime ${RUNTIME} --evgen_memory ${MEMORY}"
echo $COMMAND
$COMMAND
