pipeline {
    agent any

    tools {
        maven 'maven'
    }
    
    triggers {
    GenericTrigger(
     genericVariables: [
      [key: 'ref', value: '$.ref'],
         [key: 'PR_COMMIT_HASH', value: '$.head_commit.id'],
         [key: 'head_commit', value: '$.head_commit']
     ],
      printContributedVariables: true,
     printPostContent: true,
        
        regexpFilterText: '$head_commit', // only (?) pull requests have this field
        regexpFilterExpression: '..*' // confirms that it's a pull request
    )
  }


    stages {
        stage('Try to merge with develop and build') {
            steps {
                sh """
                git fetch --all
                git checkout develop
                git merge $PR_COMMIT_HASH
                mvn clean install
                """
            }
        }
    }
}
