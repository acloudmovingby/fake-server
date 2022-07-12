pipeline {
    agent any

    tools {
        maven 'maven'
    }
    
    triggers {
    GenericTrigger(
     genericVariables: [
      [key: 'ref', value: '$.ref'],
         [key: 'PR_COMMIT_HASH', value: '$.pull_request.head.sha'],
         [key: 'pull_request', value: '$.pull_request']
     ],
      printContributedVariables: true,
     printPostContent: true,
        
        regexpFilterText: '$PR_COMMIT_HASH',
        regexpFilterExpression: '..*' // confirms that the field exists and has some value, if not this Jenkins job won't run
    )
  }


    stages {
        stage('Try to merge with develop and build') {
            steps {
                sh """
                git fetch --all
                git checkout develop
                git pull
                git checkout -b jenkins-build-$PR_COMMIT_HASH
                git merge $PR_COMMIT_HASH
                curl --location --request POST 'https://api.github.com/repos/acloudmovingby/fake-server/statuses/$PR_COMMIT_HASH' \
--header 'Accept: application/vnd.github+json' \
--header 'Authorization: token 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' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "state":"pending",
    "context":"build"
}'
                mvn clean install
                curl --location --request POST 'https://api.github.com/repos/acloudmovingby/fake-server/statuses/$PR_COMMIT_HASH' \
--header 'Accept: application/vnd.github+json' \
--header 'Authorization: token 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' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "state":"success",
    "context":"build"
}'
                """
            }
        }
    }
}
