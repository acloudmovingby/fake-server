#!/bin/bash

JENKINS_JOB_URL=$1

echo "Sending curl call to $JENKINS_JOB_URL"
curl --silent $JENKINS_JOB_URL | grep "tooltip=\"Success" > /dev/null
CONTAINED_SUCCESS=$?

echo "Grepping for the word success in the Jenkins Job status page: $CONTAINED_SUCCESS"


