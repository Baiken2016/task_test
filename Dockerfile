FROM python

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements .


RUN pip install -r requirements

COPY . .


