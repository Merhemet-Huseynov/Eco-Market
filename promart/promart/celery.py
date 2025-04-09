from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "promart.settings")

app = Celery("promart")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.update(
    CELERY_POOL="solo",
)

app.autodiscover_tasks()









