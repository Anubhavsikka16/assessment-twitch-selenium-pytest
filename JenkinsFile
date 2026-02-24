pipeline {
    agent any

    environment {
        CHROME_OPTIONS = "--headless=new"
    }

    stages {

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    sh '''
                        .venv/bin/python -m pytest tests/ \
                        -n 4 \
                        --dist=loadfile \
                        --alluredir=allure-results
                    '''
                }
            }
        }
    }

    post {
        always {
            allure results: [[path: 'allure-results']]
        }

        cleanup {
            sh 'rm -rf .venv'
        }
    }
}