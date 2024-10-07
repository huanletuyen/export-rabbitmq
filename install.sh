#!/bin/bash
# install requirement packet 
pip3 install -r requirements.txt
#move python3 to lib system
cp blue_rabbitMQ.py /usr/bin/blue_rabbitMQ.py
# add permision excute for blue-rabbitmq.sh and move it to folder bin
chmod +x blue-rabbitmq.sh
cp blue-rabbitmq.sh /usr/bin