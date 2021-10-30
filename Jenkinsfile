pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
    }
    triggers {
        pollSCM('H/2 * * * *')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'virtualenv -p python3 venv' 
                sh '. venv/bin/activate && pip3 install -r src/requirements.txt'
                echo 'Building success'                   
            }
        }
        stage('Test') {
            steps {
                echo 'Start Unit Test'                
                sh '. venv/bin/activate && python3 tests/unit_test.py'
                echo 'End Unit Test'                   
            }
        }
        stage('Release'){
            when {
                branch 'stable'
            }
            steps{
                echo 'Create new release'
            }
        }
        stage('Deploy') {
            when {
              branch 'master' 
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS'
              }
            }
            steps {                 
                echo 'Deploying....'                
            }
        }
    }
    post {
        always {
            junit 'tests/reports/*.xml'
        }
    }
}