pipeline {
    agent any

    tools {
        maven 'maven'
    }

    environment {
        GITHUB_TOKEN = credentials('GITHUB_TOKEN')
        RANDOM_NUM = "${Math.abs(new Random().nextInt())}"
        TEMP_BRANCH = "temp-branch-${RANDOM_NUM}"
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
                git checkout -b $TEMP_BRANCH
                echo "Github token is $GITHUB_TOKEN"
                echo "Setting status to pending..."
                bash jenkins-scripts/github-commit-status.sh fake-server $GITHUB_TOKEN $PR_COMMIT_HASH build pending
                git merge $PR_COMMIT_HASH
                mvn clean install
                echo "set status to success..."
                bash jenkins-scripts/github-commit-status.sh fake-server $GITHUB_TOKEN $PR_COMMIT_HASH build success
                git checkout develop
                git branch -D $TEMP_BRANCH
                """
            }
        }
    }
}
