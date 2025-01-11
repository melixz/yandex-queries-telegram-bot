# YandexQueriesTelegramBot

## Описание проекта

`YandexQueriesTelegramBot` — это асинхронный Telegram-бот, интегрированный с API Яндекс Вебмастера. Бот предоставляет доступ к данным о популярных поисковых запросах для добавленных сайтов, таких как количество показов, кликов и CTR. Проект разработан на базе библиотеки `aiogram 3.x` и поддерживает три команды для анализа запросов.

## Установка

### 1. Локальная установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ваш-репозиторий/YandexQueriesTelegramBot.git
   cd YandexQueriesTelegramBot
   ```

2. Настройте переменные окружения в файле `.env`:

   ```env
   TELEGRAM_TOKEN=ваш_токен_telegram
   YANDEX_API_KEY=ваш_oauth_токен_yandex
   YANDEX_HOST_ID=ваш_host_id
   YANDEX_USER_ID=ваш_user_id
   ```

3. Установите зависимости через `Poetry`:

   ```bash
   poetry install
   ```

4. Запустите приложение:

   ```bash
   poetry run python app/main.py
   ```

Бот запустится и начнёт принимать команды.

---

### 2. Установка через Docker

#### Шаги для запуска

1. Убедитесь, что Docker и Docker Compose установлены на вашем компьютере.

2. Настройте переменные окружения в файле `.env` в корневой директории проекта:

   ```env
   TELEGRAM_TOKEN=ваш_токен_telegram
   YANDEX_API_KEY=ваш_oauth_токен_yandex
   YANDEX_HOST_ID=ваш_host_id
   YANDEX_USER_ID=ваш_user_id
   ```

3. Запустите контейнер с помощью Docker Compose:

   ```bash
   docker-compose up --build
   ```

## Технологии

- **Python 3.12+**: Используется для написания основного кода.
- **aiogram 3.x**: Для реализации Telegram-бота.
- **aiohttp**: Для выполнения HTTP-запросов к API Яндекс Вебмастера.
- **dotenv**: Для управления переменными окружения.
- **Docker и Docker Compose**: Для контейнеризации и удобного развертывания проекта.

---

## Текущие возможности

- **Получение популярных запросов по показам** — `/top_views`: Выводит топ-10 запросов по количеству показов.
- **Получение популярных запросов по кликам** — `/top_clicks`: Выводит топ-10 запросов по количеству кликов.
- **Получение запросов с наивысшим CTR** — `/top_ctr`: Рассчитывает и выводит топ-10 запросов по CTR (клики / показы).

---

## Примечания

- Для работы с ботом необходимо, чтобы у вас был добавлен и подтверждён сайт в Яндекс Вебмастере. Подробности можно найти в [документации Яндекс Вебмастера](https://yandex.ru/dev/webmaster/doc/).
- `host_id` и `user_id` должны быть корректно настроены в файле `.env`.

---

## Ссылки

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [aiogram Documentation](https://docs.aiogram.dev/en/latest/)
- [Яндекс Вебмастер API Documentation](https://yandex.ru/dev/webmaster/doc/)
