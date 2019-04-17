## Celery routing

```bash
$ docker run -d -p 6379:6379 redis
```


### Running a celery worker handling specific queue

```bash
$ poetry run celery -A celery_routing worker -Q long --hostname=long@%h -l info --concurrency 1
```


```bash
$ poetry run python main.py
```


### Run tests

```bash
$ poetry run pytest -sv tests
```
