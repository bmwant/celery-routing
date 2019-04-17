import time

from celery_routing.queue import background_task


@background_task
def index_users():
    print('Indexing users...')
    time.sleep(7)
    print('Done')
    return 'users'


@background_task
def index_tweets():
    print('Indexing tweets...')
    time.sleep(2)
    print('Done')
    return 'tweets'
