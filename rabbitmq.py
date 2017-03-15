'''
Created on 8 de mar de 2017


Passo a passo da configuracao do RabbitMQ usando Docker Kitematic:

1. Configure a porta 15672(padrao do 'management' do container RabbitMQ) no Kitematic.
2. Conecte via SSH no Docker:
    host: 192.168.99.100
    user: docker
    password: 
3. Liste os containers do Docker:
    $ docker ps
4. Conecte ao container do RabbitMQ:
    $ docker exec -it rabbitmq bash
5. Habilite o 'management' do container:
    $ rabbitmq-plugins --offline enable rabbitmq_management
6. Saia do container precionando:
    Ctrl+P+Q
7. Restarte o container:
    $ docker restart rabbitmq
8. Acesse o 'management' do container:
    http://192.168.99.100:15672/api/
    user: guest
    password: guest

@author: alirio
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

RABBITQM_HOST = '192.168.99.100'
RABBITQM_QUEUE = 'hello'
RABBITQM_EXCHANGE = ''
RABBITQM_ROUTING_KEY = 'hello'
RABBITQM_BODY = 'Hello World!'


def consume_from_queue(host, queue, exchange, routing_key, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel = connection.channel()
    
    channel.queue_declare(queue=queue)
    
    def callback(ch, method, properties, body):
        print(" [x] Consumed %r" % body)
    
    channel.basic_consume(callback, queue=queue, no_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    
    
def publish_in_queue(host, queue, exchange, routing_key, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()
    
    channel.queue_declare(queue=queue)
    
    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body)
    print(" [x] Published " + body)
    
    connection.close()
    
    
if __name__ == '__main__':
    
    ''' Publish in queue '''
    publish_in_queue(host=RABBITQM_HOST, queue=RABBITQM_QUEUE, exchange=RABBITQM_EXCHANGE, routing_key=RABBITQM_ROUTING_KEY, body=RABBITQM_BODY+'1')
    publish_in_queue(host=RABBITQM_HOST, queue=RABBITQM_QUEUE, exchange=RABBITQM_EXCHANGE, routing_key=RABBITQM_ROUTING_KEY, body=RABBITQM_BODY+'2')
    publish_in_queue(host=RABBITQM_HOST, queue=RABBITQM_QUEUE, exchange=RABBITQM_EXCHANGE, routing_key=RABBITQM_ROUTING_KEY, body=RABBITQM_BODY+'3')
    
    ''' Consume from queue '''
    consume_from_queue(host=RABBITQM_HOST, queue=RABBITQM_QUEUE, exchange=RABBITQM_EXCHANGE, routing_key=RABBITQM_ROUTING_KEY, body=RABBITQM_BODY)
    
