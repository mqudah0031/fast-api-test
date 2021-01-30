import os
from settings import CELERY as CELERY_SETTINGS
from celery import Celery

celery = Celery('worker', broker=CELERY_SETTINGS['BROKER'], include=["worker.email"])
