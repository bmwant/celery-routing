import pytest
from celery import exceptions

from celery_routing import __version__
from celery_routing import tasks
from celery_routing.queue import background


def test_version():
    assert __version__ == '0.1.0'


def test_wrong_queue_specified():
    with pytest.raises(exceptions.QueueNotFound):
        background(tasks.wrong_queue_task)
