#!/bin/bash
echo '<<<<<<Starting>>>>>'
yum update -y

echo '<<<<<<Starting Erland>>>>>'
wget https://www.rabbitmq.com/releases/erlang/erlang-18.2-1.el6.x86_64.rpm
sudo rpm -Uvh erlang-18.2-1.el6.x86_64.rpm
rm erlang-18.2-1.el6.x86_64.rpm

echo '<<<<<<Starting RabbitMQ>>>>>'
wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.0/rabbitmq-server-3.6.0-1.noarch.rpm
sudo rpm -Uvh rabbitmq-server-3.6.0-1.noarch.rpm
rm rabbitmq-server-3.6.0-1.noarch.rpm

'<<<<<<Starting Python & Pip>>>>>'
sudo yum install -y python27
sudo yum install -y python-setuptools
sudo easy_install pika
