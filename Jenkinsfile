pipeline {
    agent any

    environment {
        IMAGE_NAME = 'nadabj/expense-tracker'
        IMAGE_TAG = 'latest'
        REGISTRY_CREDENTIALS = 'docker-hub-credentials' // ID des credentials
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/nadabouaouaja/expense-tracker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', REGISTRY_CREDENTIALS) {
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }
    }
}
