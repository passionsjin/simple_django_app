import os
from celery import Celery
from django.core.cache import cache

app = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.tasks(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
