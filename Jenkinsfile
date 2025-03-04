@Library('Shared') _
pipeline{
    agent any;
    
    stages{
        stage("code clone"){
            steps{
               script{
                   clone("https://github.com/AWS-DevOps-shubh/Hardware_Management_app.git", "main")
               }
                
            }
        }
        stage("Trivy scan file sysytem"){
            steps{
                script{
                    trivy()
                }
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
        
    }
}
