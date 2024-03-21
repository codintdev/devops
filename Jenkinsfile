node {
  stage('SCM') {
    checkout scm
    git branch: 'main', url: 'https://github.com/mvlwvr3/Prueba.git'
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'sonarqubeScaner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
