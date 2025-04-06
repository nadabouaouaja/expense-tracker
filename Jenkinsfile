pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'nadabj' // Change avec ton ID de credential
        DOCKER_IMAGE_NAME = 'nadabouaouaja/expense-tracker' // Nom de l'image
        DOCKER_IMAGE_TAG = 'latest' // Tag de l'image
    }

    stages {
        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDENTIALS}", usernameVariable: 'nadabj', passwordVariable: '197197123')]) {
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
