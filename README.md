# flask-docker
* Build the image
```
docker build -t flask-docker .
```
* Run the server either with this command below or with the docker-compose.yaml file in this project
```
docker run --name flask-docker --rm -d -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock flask-docker:latest
```
