pipeline {
    agent any

    tools {
        maven 'maven'
    }
    
    triggers {
    GenericTrigger(
     genericVariables: [
      [key: 'action', value: '$.action']
     ]
    )
  }


    stages {
        stage('build') {
            steps {
                sh """
                    git status
                    echo "********"
                    echo $action
                    ## echo $action
                """
            }
        }
    }
}
