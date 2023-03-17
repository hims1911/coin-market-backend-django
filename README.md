# coin-market-backend-django

coin-market-backend-django![Untitled Diagram drawio](https://user-images.githubusercontent.com/26831864/225870583-7dde1fcc-5599-47d9-9eb8-768172ac6020.png)





### Backend Job the will fetch the coinmarketcap records in every 5sec.

```
export DOCKER_DEFAULT_PLATFORM=linux/amd64
export DJANGO_SETTINGS_MODULE=backend.settings
```

### run the docker container

```
docker-compose up
```

In order to fetch the latest 10 records,

```
http://localhost:8000/get/
```
