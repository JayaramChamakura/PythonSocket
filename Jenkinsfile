#!groovy

pipeline {
    agent { label 'python' }
environment {
    registry = "chjayaramreddy/sockpython"
    registryCredential = "docker-hub-credentials"
    dockerImage=''
}

stages {
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
                sh "docker run --name python-socket-jenkins --detach --rm -p 11001:11001 chjayaramreddy/sockpython"
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
    
}

