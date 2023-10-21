FROM python:3.11

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .



RUN pip install -r requirements.txt

COPY . .


RUN chmod a+x docker/*.sh

ENTRYPOINT ["/fastapi_app/docker/app.sh"]
#WORKDIR src
#
#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000







