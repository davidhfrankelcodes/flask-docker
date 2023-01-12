# flask-docker
This is a simple flask project that allows users to view running containers, images, networks, and volumes. It is an educational project.

* Build the image

```
docker build -t flask-docker .
```
* Copy the .env.template to .env and run with docker-compose 

```
docker-compose up -d --build
```

# Usage
1. /containers
1. /containers/<container_id>
1. /images/
1. /images/<image_id>
1. /networks
1. /networks/<network_id>

querystring params
1. `format`: either **format=app** or format=api.
  1. format=api returns a json
  1. format=app returns the app
  1. no param returns the app
  
