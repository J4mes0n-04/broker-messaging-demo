from confluent_kafka import Consumer, KafkaException
import json

# Конфигурация консьюмера
## group.id поддержка групп потребителей
## auto.offset.reset при отсутствии офсетов
## commit() подтверждение обработки

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['orders'])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        
        # Обработка сообщения
        order = json.loads(msg.value().decode('utf-8'))
        print(f'Получен заказ: {order}')
        
        # Подтверждаем обработку
        consumer.commit(message=msg)
        
except KeyboardInterrupt:
    print('Остановка консьюмера')
finally:
    consumer.close()
