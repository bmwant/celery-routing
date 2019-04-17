from celery import group
from celery.result import ResultSet

from celery_routing import tasks
from celery_routing.queue import background


def report(async_result):
    print(
        'Task {r.task_id} finished '
        'with status {r.status} '
        'and returned {r.result}'.format(r=async_result))


def launch_tasks():
    print('Launching different types of tasks')
    r1 = background(tasks.fast_task, x=5, y=10)
    r1.then(report)

    r2 = background(tasks.long_task, 42)
    r2.then(report)

    r3 = background(tasks.default_task)
    r3.then(report)

    r4 = background(tasks.elasticsearch_task)
    r4.then(report)

    rs = ResultSet([r1, r2, r3, r4])
    rs.join()
    print('Done')


def launch_elasticsearch():
    from celery_routing.elasticsearch.tasks import index_users, index_tweets

    print('Launching indexing')
    rs = ResultSet([
        background(index_users),
        background(index_tweets),
    ])
    print(rs.join())
    print('Done')


if __name__ == '__main__':
    launch_tasks()
    # launch_elasticsearch()
