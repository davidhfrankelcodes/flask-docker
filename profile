export FLASK_DOCKER=~/Git/flask-docker
export FLASK_VENV=${VENV}/e4_flask_docker
alias flask-activate='source ${FLASK_VENV}/bin/activate'
alias flask-run='flask run --app=${FLASK_DOCKER}/app.py --host=0.0.0.0'
alias flask-build='cd ${FLASK_DOCKER} && docker-compose down && docker-compose up -d --build && cd -'
alias flask-pytest='pytest $GIT_HOME/flask-docker/tests'
