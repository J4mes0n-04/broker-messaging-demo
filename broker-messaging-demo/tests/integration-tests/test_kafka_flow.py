import unittest
from confluent_kafka import Producer, Consumer
import json
import time

## Проверяет сквозной поток данных

class TestKafkaFlow(unittest.TestCase):
    
    def setUp(self):
        self.producer = Producer({'bootstrap.servers': 'localhost:9092'})
        self.consumer = Consumer({
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'test-group',
            'auto.offset.reset': 'latest'
        })
        self.consumer.subscribe(['orders'])
    
    def test_message_flow(self):
        # Отправляем сообщение
        test_msg = {'order_id': 999, 'amount': 999.99}
        self.producer.produce(
            'orders',
            value=json.dumps(test_msg).encode('utf-8')
        )
        self.producer.flush()
        
        # Ждём и проверяем приём
        msg = self.consumer.poll(timeout=5.0)
        self.assertIsNotNone(msg)
        received = json.loads(msg.value().decode('utf-8'))
        self.assertEqual(received['order_id'], 999)
    
    def tearDown(self):
        self.consumer.close()

if __name__ == '__main__':
    unittest.main()
