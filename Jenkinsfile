pipeline {
    agent any
    environment {
        REGISTRY_CREDENTIALS = 'docker-hub-credentials'  // Nom des credentials Jenkins
        IMAGE_NAME = 'nadabouaouaja/expense-tracker'  // Nom de ton image Docker sur Docker Hub
        IMAGE_TAG = 'latest'  // Tag de l'image
    }
    tools {
        docker 'docker'  // Utiliser Docker installé automatiquement
    }
    stages {
        stage('Pousser l\'image sur Docker Hub') {
            steps {
                script {
                    // Pousser l'image vers Docker Hub en utilisant les credentials Jenkins
                    echo "Pushing Docker image to Docker Hub..."
                    docker.withRegistry('https://index.docker.io/v1/', REGISTRY_CREDENTIALS) {
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }
        stage('Test Docker') {
            steps {
                script {
                    // Tester la connectivité Docker (afficher des informations sur Docker)
                    echo "Testing Docker connectivity..."
                    sh 'docker info'
                }
            }
        }
    }
}
