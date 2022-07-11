pipeline {
    agent any

    tools {
        maven 'maven'
    }
    
    triggers {
    GenericTrigger(
     genericVariables: [
      [key: 'ref', value: '$.ref'],
         [key: 'PR_COMMIT_HASH', value: '$.head_commit.id']
     ],
      printContributedVariables: true,
     printPostContent: true
    )
  }


    stages {
        stage('build') {
            steps {
                sh """
                    git status
                    echo "********"
                    echo $ref
                    echo $PR_COMMIT_HASH
                """
            }
        }
    }
}
