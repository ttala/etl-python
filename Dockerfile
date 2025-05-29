FROM python:3.9-slim

WORKDIR /app

COPY app/ ./app
COPY app/requirements.txt .

RUN apt update && pip install app/requirements.txt

CMD ["python", "app/main.py"]
