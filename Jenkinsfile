pipeline {
    agent any
    environment {
        REGISTRY_CREDENTIALS = 'docker-hub-credentials'  // Nom des credentials Jenkins
        IMAGE_NAME = 'nadabouaouaja/expense-tracker'  // Ton nom d'image Docker Hub
        IMAGE_TAG = 'latest'  // Tag de l'image
    }
    stages {
        stage('Cloner le repo') {
            steps {
                git branch: 'main', url: 'https://github.com/nadabouaouaja/expense-tracker.git'
            }
        }
        stage('Construire l\'image Docker') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }
        stage('Pousser l\'image sur Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', REGISTRY_CREDENTIALS) {
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }
        
    stages {
        stage('Docker Test') {
            steps {
                script {
                    echo "Testing Docker connectivity..."
                    sh 'docker info'
                }
            }
        }
    }
    }
}
