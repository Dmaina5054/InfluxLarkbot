
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
    print(bucket)

    with InfluxDBClient(url=url, token=token,org='AH',debug=False) as client:

        query_api = client.query_api()
        """
        Query: using Stream
        """

        records = query_api.query_stream(f'''
            from(bucket:"{bucket}")
            |> range(start: -5m, stop: now())
            |> filter(fn: (r) => r["_measurement"] == "ping")
            |> filter(fn: (r) => r["_field"] == "percent_packet_loss")
            |> filter(fn: (r) => r["_value"] >= 100)
            |> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
            |> yield(name: "mean")''')
        if records:
            
            for record in records:
                #print(record)
                #asyncio.sleep(2)
                time.sleep(1)
                try:
                    if record["name"]:
                        rec = f'{record["host"]} {record["name"]} Building'
                    bldgkeys.append(rec)
                except Exception as e:
                    print(e)
                
                # need to implement caching
    print(bldgkeys)
    cachealert(bldgkeys)
    return None
  
    
