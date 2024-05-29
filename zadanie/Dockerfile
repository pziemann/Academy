FROM alpine:3.17 AS build-env

WORKDIR /app

COPY requirements.txt app.py config.cfg app.log /app/
COPY logs/std.log /app/logs/

RUN apk add python3 py3-pip python3-dev postgresql-dev gcc musl-dev

RUN pip3 install -r requirements.txt

EXPOSE 5005

CMD ["python3", "app.py"]