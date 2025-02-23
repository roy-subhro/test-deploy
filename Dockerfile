FROM python:3.7-slim

WORKDIR /app

COPY . /app/

CMD ["python", "app.py"]
