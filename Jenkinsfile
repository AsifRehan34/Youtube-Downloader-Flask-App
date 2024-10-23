pipeline{
    agent any
    stages{
        stage("Clone code")
        {
            steps
            {
                echo "cloning code from git hub"
                git url: "https://github.com/AsifRehan34/Youtube-Downloader-Flask-App.git", branch:"main"
            }
        }
        stage("Build")
        {
            steps{
                echo "Build the docker image"
                sh " docker build -t youtube-video-download-app ."
            }
        }
        stage("Push to Docker Hub")
        {
            steps{
                echo "pushing to docker hub"
                withCredentials([usernamePassword(credentialsId:"Docker-Hub",passwordVariable:"DockerHubPass",usernameVariable:"DockerHubUser")])
                {
                    sh " docker tag youtube-video-download-app ${env.DockerHubUser}/youtube-video-download-app:latest"
                    sh " docker login -u ${env.DockerHubUser} -p ${env.DockerHubPass}"
                    sh "docker push ${env.DockerHubUser}/youtube-video-download-app:latest"
                }
            }
        }
        stage("Deploy")
        {
            steps
            {
                echo "Deploying the docker container to AWS "
                sh " docker-compose down && and docker-compose up -d"
            }
        }
    }
}