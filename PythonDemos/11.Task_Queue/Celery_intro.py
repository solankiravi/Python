from celery import Celery
from time import sleep

app = Celery('Celery_intro',broker=r'amqp://admin:admin@localhost:5672/')


@app.task
def reverse(text):
    sleep(5)
    return text[::-1]