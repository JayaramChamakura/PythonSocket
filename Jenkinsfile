#!groovy

pipeline {
    agent { label 'python' }
environment {
    registry = "chjayaramreddy/sockpython"
    registryCredential = "docker-hub-credentials"
    dockerImage=''
}

stages {
	stage ('Start') {
		steps {
			slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
		}
	}	
	stage('Compile') {
                steps {
                        echo "stage 1: compiling project"

                        sh "python -m compileall *.py"
                }
        }
        stage('Unit tests') {
            steps {
                echo "stage 2:  Unit testing the application"
		sh "python -m unittest test_server"
            }
        }
        stage('Build Docker image') {
            steps {
                echo "stage 3: docker image build"
                sh "ls"
                sh "pwd"
//                sh 'docker build -t chjayaramreddy/sockpython .'
                script {
          		dockerImage = docker.build registry + ":$BUILD_NUMBER"
        	}
	    }
        }
        stage('Run Docker image') {
            steps {
                echo "stage 4:  run Docker image"
                sh "docker stop python-socket-jenkins"
		sh "docker run --name python-socket-jenkins --hostname=cineserver --detach --rm -p 11001:11001 chjayaramreddy/sockpython"
            }
        }
        stage('Push Docker image') {
            	steps {
                	echo "stage 5: Push the image to registry"
                   //sh "docker push chjayaramreddy/sockpython"
        		script {
          			docker.withRegistry( '', registryCredential ) {
            			dockerImage.push()
 	         		}
        		}
        	}
	}
}       	
post {
	success {
		slackSend (color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
      	}
	failure {
		slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
	}
}
      	
    
}

