pipeline {
    agent any

    tools {
        maven 'maven'
    }
    
    triggers {
    GenericTrigger(
     genericVariables: [
      [key: 'ref', value: '$.ref']
     ]
    )
  }


    stages {
        stage('build') {
            steps {
                sh """
                    git status
                    echo "********"
                    echo $ref
                    ## echo $action
                """
            }
        }
    }
}
