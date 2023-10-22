FROM python:3.11

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .


RUN apt-get update \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

COPY . .


RUN chmod a+x docker/*.sh

ENTRYPOINT ["/fastapi_app/docker/app.sh"]







