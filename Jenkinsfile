pipeline {
    agent any
    triggers { pollSCM('* * * * *')}

    stages {
        //implicit checkout stage
        //stage('Checkout') {
        //     steps {
        //     // Checkout the repository from GitHub
        //     git branch: 'main', url: 'git@github.com:BrambergerMax/jenkins_tutorial_repo.git'
        //  }
        //}
        stage('Build Conda Environment') {
            steps {
                // Build a Conda environment using the provided YAML file
                bat '''call conda env create --file environment_test.yml --force
                    call conda activate jenkins_learn_ci_cd
                    call pip install -r requirements.txt'''
            }
        }
        stage('Run Pytest') {
            steps {
                // Run Pytest
                bat  '''call conda activate jenkins_learn_ci_cd
                        call python -m pytest --verbose --junit-xml reports/unit_tests.xml
                        '''
            }
            post{
                always{
                    junit allowEmptyResults: true, testResults: 'reports/unit_tests.xml'
                }
            }
        }
    }
}