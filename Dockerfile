FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser -D myuser
USER myuser

CMD gunicorn --bind 0.0.0.0:$PORT wsgi