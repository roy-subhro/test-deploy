FROM python:3.7-slim

WORKDIR /app

COPY . /app/

EXPOSE 80

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

CMD ["--host=0.0.0.0", "--port=80"]
