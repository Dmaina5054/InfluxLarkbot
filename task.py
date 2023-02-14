from celery import Celery
from celery.schedules import crontab
import time
from queryinflux import queryInflux
import asyncio
from celery import chain
from celery.utils.log import get_task_logger
from dotenv import load_dotenv
import os 



load_dotenv()


BROKER_ENDPOINT = os.getenv('BROKEN_ENDPOINT')
app = Celery('task',broker="amqp://maina:maina@localhost:5672//",result_backend = 'rpc://')
#app.conf.timezone = 'Africa/Nairobi'
app.conf.beat_schedule = {
    'fetch  influxquery results':{
        'task': 'MAINTASK',
        'schedule': 400,
    }
}

# app.task_acks_late = True
# app.worker_prefetch_multiplier = 1

#creating logger
celery_log = get_task_logger(__name__)
buckets = ['regionone']
eastbuckets = ['easttwo']
@app.task(name='MAINTASK')
def main():    
    for bucket in buckets:
        data = queryInflux(bucket)
    celery_log.info("Finished Processing")
        

    return 'OK'
@app.task(name='EAST-BUCKET-TASK')
def eastregion():
    for bucket in eastbuckets:
        data = queryInflux(bucket)
    celery_log.info("Finished processing east bucket")
    return 'DONE!'
