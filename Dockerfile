FROM python:3

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
#WORKDIR src
#
#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000






