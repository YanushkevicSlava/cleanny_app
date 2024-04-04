FROM python:3.11-alpine3.18

COPY requirements.txt /temp/requirements.txt
COPY cleanny /cleanny
WORKDIR /cleanny
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password cleanny-user

USER cleanny-user