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
- `curl -X POST http://localhost:5001/forward` → получит данные от service-a и (опционально) отправит их в ваш проект

Чтобы включить отправку в ваш реальный проект, раскомментируйте переменную окружения `PROJECT_URL` в `docker-compose.yml` и укажите URL вашего сервиса.

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

## Идея взаимодействия с вашим проектом

- `service-a` формирует полезную нагрузку с данными о студенте (можно менять через env).  
- `service-b` забирает эту нагрузку и отправляет POST в ваш проект по адресу `PROJECT_URL` (если он задан).

## Где сделать скриншоты для отчёта
1. Содержимое репозитория на GitHub (структура папок).
2. `docker compose up --build` в терминале (видно, как собираются образы и стартуют контейнеры).
3. Открытый `http://localhost:5000/payload` в браузере.
4. Результат `curl -X POST http://localhost:5001/forward` в терминале.
5. (Опционально) Логи `service-b`, где видно успешную отправку в ваш проект.

## Лицензия
MIT
