pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'hi' // Mettre à jour avec l'ID du credential correct
        DOCKER_IMAGE_NAME = 'nadabouaouaja/expense-tracker' // Nom de l'image
        DOCKER_IMAGE_TAG = 'latest' // Tag de l'image
    }

    stages {
        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDENTIALS}", usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat """
                            docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%
                        """
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    bat """
                        docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}
                    """
                }
            }
        }
    }
}
