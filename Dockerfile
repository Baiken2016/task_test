FROM python

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .


