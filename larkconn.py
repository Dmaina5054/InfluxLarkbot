import requests
import json
import time
import os
from dotenv import load_dotenv
import asyncio
from redis import Redis
from worklist import *

redisclient = Redis(db=1)

load_dotenv() 

webhookurl = os.getenv('webhookurl')


def sendalert(data):
<<<<<<< HEAD
<<<<<<< HEAD
  if "FIBER" in data:
    print(data)

=======
=======
>>>>>>> 21728ce (Updates to worklist)
<<<<<<< HEAD
=======
  if "FIBER" in data:
    print(data)
=======
  modifieddata = splitdata(data)
>>>>>>> 8616670 (Updates to worklist)

>>>>>>> bb0361f (test push user)
>>>>>>> 9fcba1c (test push user)
  payload = json.dumps({
    "msg_type": "post",
    "content": {
      "post": {
        "en_us": {
          #"title": f"{data.split(' ')[0]} 2218 Offline Issue",
<<<<<<< HEAD
          "title":"OFFLINE BUILDINGS AS PER IAP PING STATUS",
=======
<<<<<<< HEAD
          "title":"2218 OFFLINE ISSUE",
=======
          "title":"OFFLINE BUILDINGS AS PER IAP PING STATUS",
>>>>>>> bb0361f (test push user)
>>>>>>> 9fcba1c (test push user)
          "content": [
            [
              {
                "tag": "text",
                #"text": f"""{data}"""
                "text": f"""{modifieddata}"""
              }, 
              
            ]
          ]
        }
      }
    }
  })
  headers = {
    'Content-Type': 'application/json'
  }
  if len(data) == 0:
        print('Nothing to send')
  else: 
    
    #print(data)
    return requests.request("POST", webhookurl, headers=headers, data=payload)
  
  #print(data)
  #print(f'Alerted {data}')
  

  


  
 
  

  