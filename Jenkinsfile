pipeline {
    agent any

    tools {
        maven 'maven'
    }

    stages {
        stage('build') {
            steps {
                sh 'mvn install'
                sh """
                    curl --location --request GET 'https://api.github.com/repos/acloudmovingby/fake-server/commits/846015bcfae961b49159670ae3d518454d0abae4/status' \\
                    --header 'Accept: application/vnd.github.v3+json' \\
                    --header 'Authorization: token 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' \\
                    --data-raw ''
                """
            }
        }
    }
}
