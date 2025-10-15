# Практическая работа №3.1 — простые микросервисы + Docker Compose

Два микросервиса максимально простые:

- **service-a** (Python + Flask): отдаёт JSON `/payload` с данными студента и группой.
- **service-b** (Python + Flask): получает данные от `service-a` и _по желанию_ отправляет их в ваш проект (если задан `PROJECT_URL`). Также отдаёт `/health` и принимает POST на `/forward`.

## Быстрый старт

```bash
docker compose up --build
```

Проверки:
- http://localhost:5000/health → `{"status":"ok"}`
- http://localhost:5000/payload → `{"student":"Degtyarev","group":"EFBO-02-23","timestamp_utc":"..."}`
- http://localhost:5001/health → `{"status":"ok"}`
- `curl -X POST http://localhost:5001/forward` → получит данные от service-a 

## Структура
```
microservices-practice-3_1/
├─ service-a/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ service-b/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
└─ docker-compose.yml
```

## Типовые команды

```bash
# Запуск
docker compose up --build

# Остановка и удаление контейнеров
docker compose down

# Повторная сборка
docker compose build --no-cache
```

## Идея взаимодействия с  проектом

- `service-a` формирует полезную нагрузку с данными о студенте (можно менять через env).  
- `service-b` забирает эту нагрузку и отправляет POST в ваш проект.


## Лицензия
MIT
