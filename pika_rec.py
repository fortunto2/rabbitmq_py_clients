#!/usr/bin/env python
import pika

params = pika.URLParameters('amqp://admin:LetMe@q.life2film.com')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='hello')

print (' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print (" [x] Received {}".format(body))

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
