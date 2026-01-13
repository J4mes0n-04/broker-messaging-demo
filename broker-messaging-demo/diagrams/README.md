# UML Sequence Diagrams - broker-messaging-demo

Этот каталог содержит UML sequence диаграммы для разных компонентов и сценариев проекта `broker-messaging-demo`.

## Описание диаграмм

### 1. 01-producer-flow.mmd - Workflow продюсера
**Название:** Producer Message Send Flow

**Описание:** Демонстрирует полный процесс отправки сообщения о заказе через Kafka Producer:
- Создание заказа в приложении
- Отправка сообщения в Kafka брокер
- Callback-функция для подтверждения доставки
- Ожидание подтверждения (poll и flush)
- Гарантия доставки сообщения

Используется в: `broker-messaging-demo/examples/producer/producer.py`

---

### 2. 02-consumer-flow.mmd - Workflow консьюмера
Название: Consumer Message Receive Flow

Описание: Показывает процесс получения и обработки сообщений Consumer:
- Подписка на topic 'orders'
- Непрерывный poll сообщений (loop)
- Десериализация JSON
- Обработка данных заказа
- Commit offset для отслеживания позиции чтения
- Graceful shutdown

**Используется в:** `broker-messaging-demo/examples/consumer/consumer.py`

---

### 3. 03-end-to-end-flow.mmd - Сквозной поток данных
Название: End-to-End Message Flow (Producer → Kafka → Consumer)

Описание: Полный сквозной процесс, объединяющий producer и consumer:
- Фаза 1 (синий): Продюсер отправляет сообщение
- Фаза 2 (зелёный): Консьюмер получает сообщение из Kafka
- Фаза 3 (оранжевый): Обработка и commit смещения

Показывает, как данные проходят через всю систему от создания до обработки.

---

### 4. 04-integration-test-flow.mmd - Flow интеграционного теста
Название: Integration Test Execution Flow

Описание: Демонстрирует процесс интеграционного теста:
- Setup Phase (фиолетовый): Инициализация Producer и Consumer
- Test Execution Phase (голубой): Создание и отправка тестового сообщения
- Verification Phase (зелёный): Проверка получения сообщения и валидация данных
- Cleanup Phase (оранжевый): Закрытие ресурсов

Детально показаны все assertion-проверки.

Используется в: `broker-messaging-demo/tests/integration-tests/test_kafka_flow.py`

---

### 5. **05-system-architecture.mmd** - Архитектура системы
Название: System Architecture & Components Interaction

Описание: Общая архитектура всей системы с инициализацией:
- Zookiper (Port 2181) - сервис координации
- Kafka Broker (Port 9092) - брокер сообщений
- Schema Registry (Port 8081) - реестр схем (опционально)
- Взаимодействие между компонентами при старте
- Операции клиента (produce/consume)

Используется в: `docker-compose.yml`

### Онлайн редактор
Скопируйте содержимое файла на https://mermaid.live/

