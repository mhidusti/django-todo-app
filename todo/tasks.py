from celery import shared_task
import time

@shared_task
def test():
    time.sleep(8)
    print('test')


def test1():
    time.sleep(8)
    print('test1')