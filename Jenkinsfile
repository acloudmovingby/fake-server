pipeline {
    agent any

    tools {
        maven 'maven'
    }

    environment {
        GITHUB_TOKEN = credentials('GITHUB_TOKEN')
        RANDOM_NUM = "${Math.abs(new Random().nextInt())}"
    }

    triggers {
        GenericTrigger(
                genericVariables: [
                        [key: 'ref', value: '$.ref'],
                        [key: 'PR_COMMIT_HASH', value: '$.pull_request.head.sha']
                ],
                printContributedVariables: true,
                printPostContent: true,

                regexpFilterText: '$PR_COMMIT_HASH',
                regexpFilterExpression: '..*' // confirms that the field exists and has some value...if not, this Jenkins job won't run
        )
    }


    stages {
        stage('Try to merge with develop and build') {
            steps {
                sh """
                git fetch --all
                git checkout develop
                git pull
                TEMP_BRANCH=merge-$PR_COMMIT_HASH-into-develop-$RANDOM_NUM
                git checkout -b $TEMP_BRANCH
                echo "Github token is $GITHUB_TOKEN"
                echo pwd
                echo "set status to pending..."
                git merge $PR_COMMIT_HASH
                mvn clean install
                echo "set status to success..."
                git checkout develop
                git branch -D $TEMP_BRANCH
                """
            }
        }
    }
}
