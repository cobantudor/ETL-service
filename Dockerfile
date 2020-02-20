FROM python:3.7-buster

# Install OS dependencies
RUN apt update -y && apt upgrade -y && apt install -y cron nano

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# Register crontab jobs
RUN flask crontab add

ENTRYPOINT [".docker/docker-entrypoint.sh"]