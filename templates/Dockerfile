FROM python:3.12-slim

RUN apt update && apt install -y ffmpeg && apt clean

WORKDIR /app

COPY app.py /app
COPY templates /app/templates

RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py"]
