from celery import Celery
from kombu import Queue

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y


background_task = app.task
