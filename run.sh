#!/bin/bash

# enable model
export PYTHONPATH=$PWD/models:$PYTHONPATH

# set DSID
DSID=${1}
if [[ -z ${DSID} ]]; then
    echo "DSID not provided, using 150000 as default.";
    DSID=150000;
fi

# launch job
cd workdir
Gen_tf.py --ecmEnergy=13000. --firstEvent=1 --maxEvents=1 --randomSeed=1234 --jobConfig=${DSID} --outputEVNTFile=test_DSID_${DSID}.EVNT.root
cd -
ls workdir
