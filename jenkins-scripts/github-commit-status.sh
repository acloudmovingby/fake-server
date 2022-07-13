#!/bin/bash

NUM_ARGS=5

REPO_NAME=$1
GITHUB_TOKEN=$2
COMMIT_HASH=$3
CONTEXT=$4 # the name of the status check
STATE=$5 # must be one of: 'success', 'pending', or 'failure'

if [[ $# -ne $NUM_ARGS ]]; then
  echo "$0 requires $NUM_ARGS arguments: (1) repo name, (2) github personal token, (3) commit hash, (4) name of the status check, and
  and (5) the state of that commit status (success, failure, or pending). The number of arguments provided was $#.
  For more info, see https://docs.github.com/en/rest/commits/statuses"
  exit 2
fi

if [ $STATE != "success" ] && [ $STATE != "pending" ] && [ $STATE != "failure" ] ; then
  echo "State of commit status must be one of: 'success', 'pending', or 'failure'. See https://docs.github.com/en/rest/commits/statuses"
  exit 2
fi

echo "Attempting to set the '$CONTEXT' status to '$STATE' for commit $COMMIT_HASH."

echo "Response from Github:"

curl --location --request POST "https://api.github.com/repos/acloudmovingby/$REPO_NAME/statuses/$COMMIT_HASH" \
  --header "Accept: application/vnd.github+json" \
  --header "Authorization: token $GITHUB_TOKEN" \
  --header "Content-Type: text/plain" \
  --data-raw "{
    \"state\": \"$STATE\",
    \"context\": \"$CONTEXT\"
}"

exit 0
