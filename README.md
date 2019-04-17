## Celery routing

```bash
$ docker run -d -p 6379:6379 redis
```


### Running a celery worker handling specific queue

Default/fast queue

```bash
$ poetry run celery -A celery_routing worker -Q default,fast --hostname=default@%h -l info --concurrency 1
```

Long queue

```bash
$ poetry run celery -A celery_routing worker -Q long --hostname=long@%h -l info --concurrency 1
```

Dedicated to specific package (elasticsearch) queue

```bash
$ poetry run celery -A celery_routing worker -Q elasticsearch --hostname=es@%h -l info --concurrency 1
```

```bash
$ poetry run python main.py
```


### Run tests

```bash
$ poetry run pytest -sv tests
```
