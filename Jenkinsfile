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
        
        regexpFilterText: '$head_commit',
        regexpFilterExpression: 'nothing-should-match-this'
    )
  }


    stages {
        stage('Check if it\'s a pull request') {
            steps {
                echo "Apparently job is running..."
                sh "echo $head_commit"
            }
        }
    }
}
