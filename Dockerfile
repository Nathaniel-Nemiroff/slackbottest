FROM ruby:2.5
RUN  git clone https://github.com/Nathaniel-Nemiroff/slackbottest

FROM python:2.7-slim
RUN pip install slackclient
RUN chmod +x ./slackbottest/exportscript;./slackbottest/exportscript
RUN NEMITOKEN = 'xoxb-573900660641-580144662512-NLixtWX0Ln3zDzmKnn7xlBQO';export SLACK_BOT_TOKEN = NEMITOKEN
RUN python ./slackbottest/slackbot.py
