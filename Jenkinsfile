node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'sonarqubeScaner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
  stage('Test') {
    steps {
      echo "Probando el repo"
      git branch: 'main', url: 'https://github.com/mvlwvr3/Prueba.git'
      sh '''
      ls -la
      '''
    }
  }
}
