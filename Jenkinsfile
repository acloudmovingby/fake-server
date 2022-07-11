pipeline {
    agent any

    tools {
        maven 'maven'
    }
    
    triggers {
    GenericTrigger(
     genericVariables: [
      [key: 'ref', value: '$.ref']
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
                """
            }
        }
    }
}
