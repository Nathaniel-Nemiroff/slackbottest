FROM python:2.7

RUN  echo 'ECHO WORKS'
RUN  git clone https://github.com/Nathaniel-Nemiroff/slackbottest
RUN  pip install slackclient; pip install requests

EXPOSE 80
RUN  export SLACK_BOT_TOKEN='xoxb-573900660641-580144662512-hxaBqk3aI8EtGZ8NM8S54RkR'
RUN  python ./slackbottest/slackbot.py
