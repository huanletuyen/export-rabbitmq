# RabbitMQ Queue Import/Export Tool

## Mô tả

Ứng dụng này cho phép bạn import và export các hàng đợi (queue) từ RabbitMQ. Bạn có thể xuất các Message và properties của queue ra file và sau đó import lại để sử dụng lại khi cần thiết.

## Tính năng

- **Export Queue**: Xuất các thông điệp và thuộc tính của một queue trong RabbitMQ ra file.
- **Import Queue**: Nhập lại các thông điệp và thuộc tính vào một queue trong RabbitMQ từ file.
- Hỗ trợ xác thực RabbitMQ với username và password.

## Cài đặt

Để sử dụng ứng dụng này, bạn cần cài đặt Python và một số thư viện cần thiết.

### Yêu cầu

- Python 3.6+
- `pika` (thư viện để giao tiếp với RabbitMQ)

### Cài đặt các thư viện cần thiết

Bạn có thể cài đặt và install  các thư viện cần thiết bằng lệnh:
B1: clone git về local
```bash
git clone https://github.com/huanletuyen/export-rabbitmq.git
cd export-rabbitmq
```
B2: thực hiện chạy lệnh dưới cấp quyền thực thi cho file install
```bash
chmod +x install.sh 
```
B3: Thực hiện chay lệnh install để cài đặt các thư viện cần thiết
```bash
./install.sh
```

## Sử dụng
### **Export Queue:**
```bash
blue-rabbitmq.sh --export-data --queue=QUEUE_NAME --host=HOST --username=USERNAME --password=PASSWORD --output-file=exported_messages.txt
```

Trong đó các đối số của dòng lệnh được giải thích như sau
```bash
    --export-data: Thực hiện chức năng xuất queue.
    --queue=QUEUE_NAME: Tên của queue cần export.
    --host=HOST: Địa chỉ máy chủ RabbitMQ.
    --username=USERNAME: Tên người dùng RabbitMQ.
    --password=PASSWORD: Mật khẩu của người dùng RabbitMQ.
    --output-file=OUTPUT_FILE: File để lưu các thông điệp và thuộc tính xuất ra.
```
### **Import Queue:**
```bash
blue-rabbitmq.sh --import-data --queue=QUEUE_NAME --host=HOST --username=USERNAME --password=PASSWORD --input-file=import_messages.txt
```
Trong đó các dối số được của dòng lệnh được giải thích như sau:
```bash
--import-data: Thực hiện chức năng nhập queue.
--queue=QUEUE_NAME: Tên của queue cần import.
--input-file=INPUT_FILE: File chứa các thông điệp và thuộc tính để nhập vào queue.
--host=HOST: Địa chỉ máy chủ RabbitMQ.
--username=USERNAME: Tên người dùng RabbitMQ.
--password=PASSWORD: Mật khẩu của người dùng RabbitMQ.
```

### Lưu ý
Nếu không cung cấp đối số nào khi chạy script, bạn sẽ nhận được hướng dẫn sử dụng để biết cách cung cấp các đối số cần thiết.
## Liên Hệ:
Email: habeckbka@gmail.com
