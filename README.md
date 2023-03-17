# coin-market-backend-django
backend

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
