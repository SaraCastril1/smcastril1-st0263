# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# producer.py
# This script will publish MQ message to my_exchange MQ exchange

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('54.85.196.208', 5672, '/', pika.PlainCredentials('user', 'password')))
channel = connection.channel()

channel.basic_publish(exchange='my_exchange', routing_key='', body='Test!')

connection.close()
