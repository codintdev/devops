pipeline {
    agent any
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building..."
                sh '''
                echo "Montando"
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                python3 prueba.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "Sin errores"
                '''
            }
        }
    }
}
