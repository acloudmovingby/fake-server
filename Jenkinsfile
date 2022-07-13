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
                bash jenkins-scripts/merge-then-try-build.sh $GITHUB_TOKEN $PR_COMMIT_HASH
                """
            }
        }
    }
}
