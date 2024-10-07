#!/bin/bash

# Kiểm tra số lượng đối số
if [ "$#" -eq 0 ]; then
    echo "No arguments provided. Please provide the necessary arguments."
    echo "Usage: ./blue-rabbitmq.sh --export|--import-data --number-queue=QUEUE_NAME --host=HOST --username=USERNAME --password=PASSWORD --input-file=INPUT_FILE --output-file=OUTPUT_FILE"
    exit 1
fi

# Chạy ứng dụng Python với các đối số
python3 /usr/bin/blue_rabbitMQ.py "$@"
