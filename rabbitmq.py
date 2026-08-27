#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 8 de mar de 2017

@author: alirio
'''


import pika


RABBITMQ_HOST = '127.0.0.1'
RABBITMQ_QUEUE = 'hello'
RABBITMQ_EXCHANGE = ''
RABBITMQ_ROUTING_KEY = 'hello'
RABBITMQ_BODY = 'Hello World!'


def consume_from_queue(host, queue, exchange, routing_key, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel = connection.channel()
    
    channel.queue_declare(queue=queue, durable=True)
    
    def callback(ch, method, properties, body):
        print(" [x] Consumed %r" % body)
    
    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        connection.close()
    
    
def publish_in_queue(host, queue, exchange, routing_key, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()
    
    channel.queue_declare(queue=queue, durable=True)
    
    channel.basic_publish(
        exchange=exchange,
        routing_key=routing_key,
        body=body,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent)
    )
    print(" [x] Published " + body)
    
    connection.close()
    
    
if __name__ == '__main__':
    
    ''' Publish in queue '''
    publish_in_queue(host=RABBITMQ_HOST, queue=RABBITMQ_QUEUE, exchange=RABBITMQ_EXCHANGE, routing_key=RABBITMQ_ROUTING_KEY, body=RABBITMQ_BODY + '1')
    publish_in_queue(host=RABBITMQ_HOST, queue=RABBITMQ_QUEUE, exchange=RABBITMQ_EXCHANGE, routing_key=RABBITMQ_ROUTING_KEY, body=RABBITMQ_BODY + '2')
    publish_in_queue(host=RABBITMQ_HOST, queue=RABBITMQ_QUEUE, exchange=RABBITMQ_EXCHANGE, routing_key=RABBITMQ_ROUTING_KEY, body=RABBITMQ_BODY + '3')
    
    ''' Consume from queue '''
    consume_from_queue(host=RABBITMQ_HOST, queue=RABBITMQ_QUEUE, exchange=RABBITMQ_EXCHANGE, routing_key=RABBITMQ_ROUTING_KEY, body=RABBITMQ_BODY)
    
