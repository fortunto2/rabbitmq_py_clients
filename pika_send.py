#!/usr/bin/env python
import pika

# connection = pika.BlockingConnection(pika.ConnectionParameters(
#         host='amqp://admin:LetMe!n@q.life2film.com'))
params = pika.URLParameters('amqp://admin:LetMe@q.life2film.com')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World from Rustam!')

print (" [x] Sent 'Hello World!'")

connection.close()
World
