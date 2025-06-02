FROM python:3.9-slim

WORKDIR /app

COPY app/ /app/

RUN apt update && pip install -r requirements.txt

CMD ["python", "main.py"]
