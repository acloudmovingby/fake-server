pipeline {
    agent any

    tools {
        maven 'maven'
    }
    
    triggers {
    GenericTrigger(
     genericVariables: [
      [key: 'everything', value: '$'],
         [key: 'action', value: '$.action']
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
                    echo $action
                """
            }
        }
    }
}
