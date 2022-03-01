
import datetime as datetime
from distutils.log import debug
import sys
import time
import os
from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS
from larkconn import sendalert
import asyncio
import csv
from cachealert import cachealert
from celery import Celery
from redis import Redis



load_dotenv()

token = os.getenv('token')
url = os.getenv('url')

redisclient = Redis(db=1)
bldgkeys = []

def queryInflux(bucket):

    with InfluxDBClient(url=url, token=token,org='AH',debug=False) as client:

        query_api = client.query_api()
        """
        Query: using Stream
        """

        records = query_api.query_stream(f'''
            from(bucket:"{bucket}")
            |> range(start: -30m, stop: now())
            |> filter(fn: (r) => r["_measurement"] == "ping")
            |> filter(fn: (r) => r["_field"] == "percent_packet_loss")
            |> filter(fn: (r) => r["_value"] >= 100)
            |> aggregateWindow(every: 15m, fn: mean, createEmpty: false)
            |> yield(name: "mean")
            |> unique(column: "name")
            ''')
        if records:
    
            for record in records:
                asyncio.sleep(3)
                rec = f'{record["host"]} {record["name"]} Building'
                # need to implement caching
                cachealert(rec)
                
            
            for key in redisclient.scan_iter():
                bldgkeys.append(key.decode('utf-8'))
            sendalert(bldgkeys)
            bldgkeys.clear()
        else:
            return None
