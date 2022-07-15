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
                        [key: 'PR_COMMIT_HASH', value: '$.pull_request.head.sha'],
                        [key: 'TARGET_BRANCH', value: '$.pull_request.base.ref']
                ],
                printContributedVariables: true,
                printPostContent: true,

                regexpFilterText: '$PR_COMMIT_HASH',
                regexpFilterExpression: '..*' // confirms that the field exists and has some value...if not, this Jenkins job won't run
        )
    }


    stages {
        
        stage('Set statuses to pending') {
            steps {
                sh """
                bash jenkins-scripts/github-commit-status.sh fake-server $GITHUB_TOKEN $PR_COMMIT_HASH dbup pending
                bash jenkins-scripts/github-commit-status.sh fake-server $GITHUB_TOKEN $PR_COMMIT_HASH ATs pending
                bash jenkins-scripts/github-commit-status.sh fake-server $GITHUB_TOKEN $PR_COMMIT_HASH "Downstream merge" pending
                """
            }
        }
        
        stage('Try to merge with develop and build') {
            steps {
                sh """
                bash jenkins-scripts/merge-then-try-build.sh $GITHUB_TOKEN $PR_COMMIT_HASH
                """
            }
        }
        
        stage('Run dbup') {
            steps {
                sh """
                bash jenkins-scripts/github-commit-status.sh fake-server $GITHUB_TOKEN $PR_COMMIT_HASH dbup success
                sleep 3
                """
            }
        }
        
        stage('Run ATs') {
            steps {
                sh """
                bash jenkins-scripts/github-commit-status.sh fake-server $GITHUB_TOKEN $PR_COMMIT_HASH ATs success
                """
            }
        }
        
        stage('Merge and build downstream branches') {
            steps {
                sh """
                bash jenkins-scripts/github-commit-status.sh fake-server $GITHUB_TOKEN $PR_COMMIT_HASH "Downstream merge" success
                """
            }
        }
    }
}
