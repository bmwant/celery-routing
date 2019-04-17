from celery import Celery
from kombu import Queue


app = Celery('celery_routing')

# Configure from settings
# todo (misha): load from settings.py
# app.config_from_object('celeryconfig')
app.conf.task_serializer = 'json'
CELERY_REDIS_ENDPOINT = '127.0.0.1'
app.conf.broker_url = 'redis://{}/0'.format(CELERY_REDIS_ENDPOINT)
app.conf.result_backend = 'redis://{}/1'.format(CELERY_REDIS_ENDPOINT)

# Configure queues
app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_exchange_type = 'direct'
app.conf.task_default_routing_key = 'task'
app.conf.task_create_missing_queues = False

app.conf.task_queues = (
    Queue('default', routing_key='task'),
    Queue('elasticsearch', routing_key='es'),
    Queue('fast', routing_key='fast'),
    Queue('long', routing_key='long'),
)

app.autodiscover_tasks([
    'celery_routing',
    'celery_routing.elasticsearch',
])

background_task = app.task


def background(task, *args, **kwargs):
    return task.delay(*args, **kwargs)
