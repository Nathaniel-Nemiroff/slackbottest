FROM python:2.7

RUN  echo 'ECHO WORKS'
RUN  git clone https://github.com/Nathaniel-Nemiroff/slackbottest
RUN  pip install slackclient; pip install requests

EXPOSE 80
RUN  python ./slackbottest/slackbot.py
