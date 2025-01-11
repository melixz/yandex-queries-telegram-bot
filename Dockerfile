# Используем базовый образ Python
FROM python:3.12-slim

# Устанавливаем зависимости для сборки
RUN apt-get update && apt-get install -y curl && apt-get clean

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Устанавливаем рабочую директорию в корень проекта
WORKDIR /app

# Копируем файлы Poetry
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости через Poetry
RUN poetry install --no-root --only main

# Копируем весь проект в контейнер
COPY app/ ./app

# Указываем команду для запуска приложения
CMD ["poetry", "run", "python", "app/main.py"]
