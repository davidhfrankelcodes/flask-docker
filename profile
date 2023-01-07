# source this file to pull in these aliases
export FLASK_DOCKER=~/Git/flask-docker
export FLASK_VENV=${VENV}/e4_flask_docker

# Turn the virtualenvironment on 
alias flask-activate='source ${FLASK_VENV}/bin/activate'
# Run tests
alias flask-pytest='cd ${FLASK_DOCKER} && pytest tests && cd -'
# Build and run the image with docker-compose
alias flask-build='cd ${FLASK_DOCKER} && docker-compose down && docker-compose up -d --build && cd -'
