pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run tests') {
            steps {
                sh 'python --version'
                sh 'python test_main.py'
            }
        }
    }

    post {
        success {
            echo '✅ Tests pasaron correctamente'
        }
        failure {
            echo '❌ Tests fallaron'
        }
    }
}
