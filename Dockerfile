FROM python:3.7-alpine
MAINTAINER mawaim org

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN python -m pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org -r /requirements.txt


RUN mkdir /mawaim
WORKDIR /mawaim
COPY ./mawaim /mawaim

RUN adduser -D mawaimuser
USER mawaimuser
