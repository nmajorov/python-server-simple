#!/bin/bash

# deploy application to openshift
#
# get full path to project dir
SCRIPT_DIR=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
#echo $SCRIPT_DIR
oc new-app  https://gitlab.com/nmajorov/python36-simple-webservice.git --image-stream=openshift/python:latest --name='pyserver'
   #-n nikolaj

