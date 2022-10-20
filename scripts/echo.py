#will act as send.py
from cgi import test
from email import message
import pika
import sys 


def testa(i):
    
    #create a connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.2'))
    channel = connection.channel()

    #creating a queue
    #also dd durability
    channel.queue_declare(queue="echoserver_two",durable=True)
    #controlled dispatch
    #one message to one worker
    

    #allow some message send to server
   
    message = f"hello {i}"

    

    #publish message
    #allow messages to be persistent
    channel.basic_publish(exchange='',
    routing_key='hello',
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

    print("|[x] sent 'Hello echo server reporting'")

    #close connection
    connection.close()

if __name__ == "__main__":
    for i in range(300):
        testa(i)