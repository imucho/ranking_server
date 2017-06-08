FROM python:3.6.1-alpine
MAINTAINER Imura Tatsuya
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD gunicorn api:api
