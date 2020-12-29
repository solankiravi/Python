from celery import Celery

app = Celery(
    '1_celery',#name of project package
    broker='amqp://guest:guest@localhost:15672'#transport://userid:password@hostname:port/virtual_host
)