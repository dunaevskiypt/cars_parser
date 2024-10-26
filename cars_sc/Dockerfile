# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Команда для запуска парсера (замени на свою)
CMD ["scrapy", "crawl", "pas_car"]
