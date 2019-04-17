from celery_routing import tasks
from celery_routing.queue import background

from celery.result import ResultSet


def report(async_result):
    print(
        'Task {r.task_id} finished '
        'with status {r.status} '
        'and returned {r.result}'.format(r=async_result))


def main():
    print('Launching different types of tasks')
    r1 = background(tasks.fast_task, x=5, y=10)
    r1.then(report)

    r2 = background(tasks.long_task, 42)
    r2.then(report)

    r3 = background(tasks.default_task)
    r3.then(report)

    r4 = background(tasks.elasticsearch_task)
    r4.then(report)

    rs = ResultSet([r1, r2, r3])
    rs.join()
    print('Done')


if __name__ == '__main__':
    main()
