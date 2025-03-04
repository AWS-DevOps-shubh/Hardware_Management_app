pipeline{
    agent any;
    
    stages{
        stage("code clone"){
            steps{
                git url: "https://github.com/AWS-DevOps-shubh/Hardware_Management_app.git", branch:"main"
                
            }
        }
        stage("code build"){
            steps{
                sh "docker build -t hardware-management ."  
                
            }
        }
        stage("code test"){
            steps{
                echo "code test"    
            }
        }
        stage("push image to docker hub"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId:"dockerHubSec",
                    passwordVariable: "dockerHubPass",
                    usernameVariable: "dockerHubUser"
                )]){
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker image tag hardware-management ${env.dockerHubUser}/hardware-management"
                sh "docker push ${env.dockerHubUser}/hardware-management:latest"
                
                }
            }
        }
        stage("code deploy"){
            steps{
                sh "docker compose up -d"
            }
        }
        
        post{
            success{
                script{
                    emailext from: 'devshubh2204@gmail.com',
                        to: 'devshubh2204@gmail.com',
                        body: 'Hii shubham your build is success',
                        subject: 'Build is successfully run'
                }
            }
        }
    }
}
