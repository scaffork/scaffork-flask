FROM python:3.7.2-stretch

WORKDIR /api

COPY . /api

RUN pip3 install --upgrade pip==18.1 && \
    pip3 install -r requirements_dev.txt