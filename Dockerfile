FROM python:3.7-buster

COPY app /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python","app.py"]