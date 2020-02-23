FROM python:3.7-buster

# Install OS dependencies
RUN apt update -y && apt upgrade -y && apt install -y cron nano

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [".docker/docker-entrypoint.sh"]