from confluent_kafka import Producer
import json
import time

# Конфигурация продюсера
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'order-producer'
}

producer = Producer(conf)

def delivery_report(err, msg):
    """Callback для подтверждения доставки"""
    if err is not None:
        print(f'Ошибка доставки: {error}')
    else:
        print(f'Сообщение доставлено в {msg.topic()} [{msg.partition()}]')

def send_order(order_id, customer_id, amount):
    ""Отправка заказа"""
    message = {
        'order_id': order_id,
        'customer_id': customer_id,
        'amount': amount,
        'timestamp': int(time.time())
    }
    
    # Отправка с callback
    producer.produce(
        'orders',
        key=str(order_id).encode('utf-8'),
        value=json.dumps(message).encode('utf-8'),
        callback=delivery_report
    )
    
    # Ожидаем доставку
    producer.poll(1)

# Тестовая отправка
if __name__ == '__main__':
    for i in range(5):
        send_order(i, f'cust_{i}', 100.0 + i * 10)
        time.sleep(1)
    
    # Ждём доставки всех сообщений
    producer.flush()
