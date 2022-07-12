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
        
        regexpFilterText: '$pull_request', // only pull requests have this field, one would assume...
        regexpFilterExpression: 'nothing-should-match-this' // confirms that the field exists and has some value, if not this Jenkins job won't run
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
                mvn clean install
                """
            }
        }
    }
}
