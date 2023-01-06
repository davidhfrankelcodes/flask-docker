export GIT_HOME=~/Git
alias flask-run='flask run --host=0.0.0.0'
alias flask-build='cd $GIT_HOME/flask-docker && docker-compose down && docker-compose up -d --build && cd -'
