#!/bin/bash

# TODO this script will break if not run from root of git repo...also, maybe write this in python...

NUM_ARGS=2
GITHUB_TOKEN=$1
PR_COMMIT_HASH=$2

TEMP_BRANCH="temp-branch-$RANDOM"

if [[ $# -ne $NUM_ARGS ]]; then
  echo "This script ($0) requires $NUM_ARGS arguments: (1) github personal token and (2) commit hash. The number of arguments provided was $#."
  exit 2
fi

git fetch --all
git checkout develop
git pull
git checkout -b $TEMP_BRANCH
git merge "$PR_COMMIT_HASH"

echo "Setting status to pending..."
bash jenkins-scripts/github-commit-status.sh fake-server "$GITHUB_TOKEN" "$PR_COMMIT_HASH" build pending
POST_TO_GITHUB=$?

if [[ POST_TO_GITHUB -ne 0 ]] ; then
  git checkout develop
  git branch -D $TEMP_BRANCH
  echo "Something went wrong when trying to update commit statuses on Github. Canceling build..."
  exit 2
fi

mvn clean install
BUILD_STATUS=$?

sleep 10

if [[ BUILD_STATUS -ne 0 ]] ; then
  echo "Build failed, setting status to 'failure'"
  bash jenkins-scripts/github-commit-status.sh fake-server "$GITHUB_TOKEN" "$PR_COMMIT_HASH" build failure
else
  echo "Build succeeded, setting status to 'success'"
  bash jenkins-scripts/github-commit-status.sh fake-server "$GITHUB_TOKEN" "$PR_COMMIT_HASH" build success
fi

git checkout develop
git branch -D $TEMP_BRANCH
