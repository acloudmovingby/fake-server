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
        
        regexpFilterText: '$head_commit'
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
