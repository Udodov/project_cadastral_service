# Использование Python 3.10
FROM python:3.10

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование файла с зависимостями в рабочую директорию
COPY requirements.txt .

# Установка зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всех файлов из текущей директории в рабочую директорию контейнера
COPY . .

# Запуск приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
