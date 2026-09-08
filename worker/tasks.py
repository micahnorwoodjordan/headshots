import os

from celery import Celery


app = Celery('tasks', broker=os.environ["CELERY_BROKER_URL"])

# stub for now
@app.task
def add(x, y):
    return x + y
