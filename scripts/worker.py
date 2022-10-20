#!/usr/bin/env python
from base64 import decode
import pika, sys, os
import json

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.2'))
    channel = connection.channel()

    channel.queue_declare(queue='echoserver_two', durable=True)
    #to rabbitmq assign one worker one message
    
    channel.basic_qos(prefetch_count=1)

    def callback(ch, method, properties, body):
        channel.basic_ack(delivery_tag=method.delivery_tag)
        bodystr = body.decode('utf-8')
        print(f" [x] Received {bodystr}")
        print("[X] Done")
        

    #consume worker from queue
    channel.basic_consume(queue='hello', on_message_callback=callback)
    #setting acknowledgement
    

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            


