import time

from celery_routing.queue import background_task


@background_task(queue='fast')
def fast_task(x, y):
    print('Starting quick task...')
    time.sleep(1)
    print('Completed')
    return x + y


@background_task(routing_key='long', exchange='default')
def long_task(x):
    print('Processing heavy data...')
    time.sleep(10)
    print('Completed')
    return x


@background_task
def default_task():
    print('Executing a task...')
    time.sleep(3)
    print('Completed')
    return 1


@background_task(routing_key='es', exchange='default')
def elasticsearch_task():
    print('Indexing from different package...')
    time.sleep(5)
    print('Completed')
    return True


@background_task(queue='missing')
def wrong_queue_task():
    return -1
