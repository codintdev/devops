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
      sh '''
      ls -la
      '''
    }
  }
}
