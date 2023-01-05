# flask-docker
* Build the image
```
docker build -t flask-docker .
```
* Run the server
```
docker run --rm -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock flask-docker:latest
```
