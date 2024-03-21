pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building..."
                sh '''
                echo "Montando lo necesario correctamente..."
                '''
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                python3 prueba.py
                ls -l
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo "SonarQube"
                def scannerHome = tool 'sonarqubeScaner';
                withSonarQubeEnv() {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
    }
}
