#!/usr/bin/python

import pika, sys

credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost",
                                        credentials = credentials)
conn_broker = pika.BlockingConnection(conn_params) #/(hwp.1) Establish connection to broker


channel = conn_broker.channel() #/(hwp.2) Obtain channel

channel.exchange_declare(exchange="hello-exchange", #/(hwp.3) Declare the exchange
                         exchange_type="direct",
                         passive=False,
                         durable=True,
                         auto_delete=False)

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain" #/(hwp.4) Create a plaintext message

channel.tx_select()
channel.basic_publish(body=msg,
                      exchange="hello-exchange",
                      properties=msg_props,
                      routing_key="hola") #/(hwp.5) Publish the message
channel.tx_commit()
