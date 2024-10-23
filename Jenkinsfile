pipeline{
    agent any
    stages{
        stage("Clone code")
        {
            steps
            {
                echo "cloning code from git hub"
            }
        }
        stage("Build")
        {
            steps{
                echo "Build the docker image"
            }
        }
        stage("Push to Docker Hub")
        {
            steps{
                echo "pushing to docker hub"
            }
        }
        stage("Deploy")
        {
            steps
            {
                echo "Deploying the docker container to AWS "
            }
        }
    }
}