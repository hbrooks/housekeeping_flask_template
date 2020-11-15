FROM python:3.6

RUN mkdir /usr/src/my_api
WORKDIR /usr/src/my_api

RUN pip install --upgrade pip
RUN pip3 install virtualenv
RUN pip3 install zappa

COPY my_api/requirements.txt /usr/src/my_api/requirements.txt
RUN pip3 install -r /usr/src/my_api/requirements.txt

WORKDIR /usr/src/my_api/src
