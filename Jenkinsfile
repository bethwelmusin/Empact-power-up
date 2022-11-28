pipeline{
    agent any
    stages {

        stage('Setup Python ENV'){   
      steps  {
            sh '''
            chmod +x env_setup.sh
            ./env_setup.sh
            '''}
        }
        stage('Setup Gunicorn'){
            steps {
                sh '''
                chmod +x gunicorn.sh
                ./gunicorn.sh
                '''
            }
        }
        stage('Run TestCases'){
            steps {
                sh '''
                chmod +x run_tests.sh
                ./run_tests.sh
                '''
            }
        }
        stage('Setup NGINX'){
            steps {
                sh '''
                chmod +x nginx.sh
                ./nginx.sh
                '''
            }
        }
        stage('Deploy'){
            steps {
                echo "Deployed to production"
            }
        }
    }
}