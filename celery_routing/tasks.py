import time

from celery_routing.queue import background_task


@background_task
def fast_task(x, y):
    return x + y


@background_task(routing_key='long')
def long_task(x):
    return x


@background_task
def default_task(x, y):
    return x + y


@background_task
def elasticsearch_task():
    return


@background_task(queue='missing')
def wrong_queue_task():
    return -1
