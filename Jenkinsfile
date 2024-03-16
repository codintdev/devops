pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building..."
                sh '''
                echo "Montando los requerimentos..."
                '''
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
                echo 'Deliver....'
                sh '''
                echo "Sin errores. Salida exitosa..."
                '''
            }
        }
    }
}
