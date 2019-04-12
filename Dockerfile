FROM python:2.7

WORKDIR /server
COPY . /server


EXPOSE 8000
ENV NAME sbt

RUN python server.py
#CMD ['python', 'server.py']
