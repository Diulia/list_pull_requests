FROM python:3.9-slim-buster

WORKDIR /opt/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

