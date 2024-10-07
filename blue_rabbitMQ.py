import argparse
import pika
import sys
import json

# Hàm xuất (export) queue từ RabbitMQ và lưu vào file
def export_queue(rabbitmq_host, queue_name, username, password, output_file):
    credentials = pika.PlainCredentials(username, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host, credentials=credentials))
    channel = connection.channel()

    # Kiểm tra xem queue đã tồn tại
    try:
        channel.queue_declare(queue=queue_name, durable=True, passive=True)  # passive=True để kiểm tra mà không tạo
    except pika.exceptions.ChannelClosed:
        print(f"Queue '{queue_name}' does not exist.")
        connection.close()
        return  # Thoát nếu queue không tồn tại

    # Mở file để ghi thông điệp và thuộc tính
    with open(output_file, 'w') as file:
        while True:
            method_frame, properties, body = channel.basic_get(queue=queue_name, auto_ack=False)
            if method_frame:
                message = body.decode()
                output = f"Message: {message}, Properties: {json.dumps(properties.__dict__)}"  # Lưu properties ở định dạng JSON
                print(output)
                file.write(output + '\n')
            else:
                print("No more messages in the queue.")
                break

    connection.close()

# Hàm nhập (import) queue vào RabbitMQ
def import_queue(rabbitmq_host, queue_name, username, password, input_file):
    credentials = pika.PlainCredentials(username, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host, credentials=credentials))

    try:
        channel = connection.channel()

        # Kiểm tra xem queue đã tồn tại
        try:
            channel.queue_declare(queue=queue_name, durable=True, passive=True)
            print(f"Queue '{queue_name}' exists.")
        except pika.exceptions.ChannelClosed:
            print(f"Queue '{queue_name}' does not exist. Creating it.")
            channel.queue_declare(queue=queue_name, durable=True)

        # Đọc thông điệp và thuộc tính từ file và gửi vào queue
        with open(input_file, 'r') as file:
            for line in file:
                parts = line.split(", Properties: ")
                if len(parts) == 2:
                    message = parts[0].replace("Message: ", "").strip()
                    properties_str = parts[1].strip()
                    # Chuyển đổi properties từ JSON về dict
                    properties = json.loads(properties_str)  # Sử dụng json.loads thay cho eval

                    # Gửi thông điệp vào queue với các thuộc tính
                    channel.basic_publish(exchange='',
                                          routing_key=queue_name,
                                          body=message,
                                          properties=pika.BasicProperties(**properties))

                    print(f"Imported message: {message} with properties: {properties}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

# Hàm chính
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for importing/exporting RabbitMQ queues.')
    parser.add_argument('-e', '--export-data', action='store_true', help='Export data from the queue')
    parser.add_argument('-i', '--import-data', action='store_true', help='Import data into the queue')
    parser.add_argument('--queue', type=str, required=True, help='Name of the queue')
    parser.add_argument('--host', type=str, default='localhost', help='RabbitMQ server host (default: localhost)')
    parser.add_argument('--username', type=str, required=True, help='Username for RabbitMQ')
    parser.add_argument('--password', type=str, required=True, help='Password for RabbitMQ')
    parser.add_argument('--input-file', type=str, help='File to import messages from')
    parser.add_argument('--output-file', type=str, help='File to save exported messages')

    # Kiểm tra nếu không có đối số nào được truyền vào
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    # Xuất queue và lưu vào file
    if args.export_data:
        if not args.output_file:
            print("No output file specified. Use --output-file to specify the file to save messages.")
            sys.exit(1)
        export_queue(args.host, args.queue, args.username, args.password, args.output_file)

    # Nhập queue
    if args.import_data:
        if not args.input_file:
            print("No input file specified. Use --input-file to specify the file to import messages.")
            sys.exit(1)
        import_queue(args.host, args.queue, args.username, args.password, args.input_file)