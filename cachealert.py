from larkconn import sendalert
import asyncio
import csv
import json
from redis import Redis

from dotenv import load_dotenv
from collections import  Counter

import requests
import json
import time
import os

import asyncio
import numpy as np


load_dotenv() 

webhookurl = os.getenv('webhookurl')
redisclient = Redis(db=1)

#use as factory function
def cachealert(alrt):
   # print(f'{alrt} will be cached...')
    itema = unique(alrt)
    #print(itema)
    return cacher(itema)
    
#only get unique from list
def unique(listel):
    x = np.array(listel)
    
    return np.unique(x)

allalarms= []
def cacher(itemms):
    ts = itemms.tolist()
<<<<<<< HEAD
 
=======
<<<<<<< HEAD
=======
 
>>>>>>> bb0361f (test push user)
>>>>>>> 9fcba1c (test push user)
    for d in ts:
        host = f'{d.split()[0]}'
        alarmkey = f"{host+ ':' + d.split()[1]}"
        bldgname = f'{d.split()[1]}'
        alarmserial = {alarmkey:bldgname}
        
        if redisclient.hgetall(alarmkey):
            print('incache')
        else:    
            pipe = redisclient.pipeline()
            print('caching')
            pipe.hmset(alarmkey,alarmserial)
            pipe.expire(alarmkey,1800)
            print('Cached')
            pipe.execute()
<<<<<<< HEAD
            #print(alarmkey)

            print(alarmkey)
            allalarms.append(alarmkey)

=======
<<<<<<< HEAD
            
            allalarms.append(alarmkey)
=======
            #print(alarmkey)

            print(alarmkey)
            allalarms.append(alarmkey)

>>>>>>> bb0361f (test push user)
>>>>>>> 9fcba1c (test push user)
            
    sendalert(allalarms)
    print(f'Before clear..{allalarms}')
    
<<<<<<< HEAD
<<<<<<< HEAD

=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> d6ee04f (updates on cache)
>>>>>>> 1825c19 (updates on cache)
    try:
        allalarms.clear()
        print(f'After clear...{allalarms}')
        return None 
    except  Exception as e:
        print(e)
<<<<<<< HEAD
=======

>>>>>>> bb0361f (test push user)
<<<<<<< HEAD
>>>>>>> 9fcba1c (test push user)
=======
=======
>>>>>>> d6ee04f (updates on cache)
>>>>>>> 1825c19 (updates on cache)
   
                

   
    