pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        GIT_REPO = "https://github.com/zDR34M/jenkins-test.git"
        BRANCH = "main"
        IMAGE = "64rq/flask-app"
    }
    stages{
        stage("Docker Login") {
            steps{
                // Add --password-stdin to run docker login command non-interactively
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'echo "Login success to Docker"'
            }
        }
        
        stage("Checkout git"){
            steps{
                sh 'echo "Checkout from github . . ."'
                sh 'git clone $GIT_REPO'
            }
        }

        stage("Build & Push Dockerfile") {
            steps {
                sh """
                echo "Starting to build the image . . ."
                cd jenkins-test/
                docker build -t $IMAGE:latest .
                docker push $IMAGE
                docker run -d --name flask-app -p 5000:80 $IMAGE
                """
            }

            post {
                success {
                    echo "App is up . . ."
                }

                failure {
                    echo "Faild to start the app . . ."
                }
            }
        }
    }
}