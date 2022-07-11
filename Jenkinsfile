pipeline {
    agent any

    tools {
        maven 'maven'
    }
    
    triggers {
    GenericTrigger(
     genericVariables: [
      [key: 'everything', value: '$']
     ]
    )
  }

    stages {
        stage('build') {
            steps {
                sh """
                    git status
                    echo $everything
                    echo "********"
                    ## echo $action
                """
            }
        }
    }
}
