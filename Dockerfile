FROM ruby:2.5
RUN  git clone https://github.com/Nathaniel-Nemiroff/slackbottest

FROM python:2.7-slim
RUN pip install slackclient
RUN export SLACK_BOT_TOKEN = 'xoxb-573900660641-580144662512-nYR9J6zX89dIrkIh7Ad4gHMy'
RUN python ./slackbottest/slackbot.py
