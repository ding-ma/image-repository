FROM python:3.8

# set environment variables
ENV DEBUG 0
ENV PORT 8000

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED 1
# prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1 

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 3 --threads 3 --timeout 100 main:app  --access-logfile -