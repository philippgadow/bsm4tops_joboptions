#!bin/bash

# Job submission for DESY HTCondor - copy to project directory and adapt to your needs
JOBNAME="EVGEN_bsm4tops_oncemorewithfeeling"
# DSIDS="150000 150001 150002 150003 150004 150005 150006 150007 150008 150009 150010 150011 150012 150013 150014 150015 150016 150017 150018 150019 150020 150021 150022 150023" #DSIDs in job option directory
# DSIDS="151000 151001 151002 151003 151004 151005 151006 151007 151008 151009 151010 151011 151012 151013 151014 151015 151016 151017 151018 151019 151020 151021 151022 151023 151024 151025 151026 151027 \
#        152000 152001 152002 152003 152004 152005 152006 152007 152008 152009 152010 152011 152012 \
#        153000 153001 153002 153003 153004 153005 153006 153007 153008 153009 153010 153011 153012 \
#        154000 154001 154002 154003 154004 154005 154006 154007 154008 154009 154010 154011 154012 154013 154014 154015 154016 154017 154018 154019 154020 154021 154022 154023 154024 154025 154026 154027 \
#        155000 155001 155002 155003 155004 155005 155006 155007 155008 155009 155010 155011 155012 155013 155014 155015 155016 155017 155018 155019 155020 155021 155022 155023 155024 155025 155026 155027" #DSIDs in job option directory

# DSIDS="150018 150019 150020 150021 150022 150023"
DSIDS="154000 154001 154002 154003 154004 154005 154006 154007 154008 154009 154010 154011 154012 154013 154014 154015 154016 154017 154018 154019 154020 154021 154022 154023 154024 154025 154026 154027 \
       155000 155001 155002 155003 155004 155005 155006 155007 155008 155009 155010 155011 155012 155013 155014 155015 155016 155017 155018 155019 155020 155021 155022 155023 155024 155025 155026 155027" #DSIDs in job option directory


EVENTS=10000               #Events per job
NJOBS=1                    #Number of jobs per DSID
RUNTIME="03:00:00"         #Run time per job HH:MM:SS
MEMORY=2000                #Memory per job in MB
MODELSDIR=$PWD/models

cd batch_submission
COMMAND="python SubmitMC/python/submit.py --jobName ${JOBNAME} --engine HTCONDOR --eventsPerJob ${EVENTS} --nJobs ${NJOBS} -r ${DSIDS} --noBuildJob --modelsDir ${MODELSDIR} --accountinggroup af-atlas --evgen_runtime ${RUNTIME} --evgen_memory ${MEMORY}"
echo $COMMAND
$COMMAND
