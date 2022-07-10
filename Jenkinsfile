pipeline {
    agent any

    tools {
        maven 'maven'
    }

    stages {
        stage('build') {
            steps {
                sh """
                    git status
                """
            }
        }
    }
}
