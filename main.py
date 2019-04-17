from celery_routing import tasks
from celery_routing.queue import background


def main():
    r = background(tasks.wrong_queue_task)
    # r = background(tasks.long_task, 10)
    # print(r.status)
    # print(r.result)


if __name__ == '__main__':
    main()
