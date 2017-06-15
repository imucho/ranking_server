FROM python:3.6.1-alpine
MAINTAINER Imura Tatsuya
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN apk add --update --no-cache mariadb-client-libs && apk add --no-cache --virtual .build-deps mariadb-dev gcc musl-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del .build-deps
EXPOSE 8000
CMD gunicorn api:api
