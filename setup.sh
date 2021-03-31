#!/bin/bash

export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh

MYRELEASE="AthGeneration,21.6.61,here"

rm -rf workdir
mkdir workdir
cp -r 150xxx/* workdir/
cp -r 151xxx/* workdir/
cp -r 152xxx/* workdir/
cp -r 153xxx/* workdir/
cp -r 154xxx/* workdir/
cp -r 155xxx/* workdir/
cd workdir
asetup ${MYRELEASE}
cd -
