FROM ruby:2.5
RUN  git clone https://github.com/Nathaniel-Nemiroff/slackbottest

RUN pip install slackclient; export SLACK_BOT_TOKEN = 'xoxb-573900660641-580144662512-nYR9J6zX89dIrkIh7Ad4gHMy';python ./slackbottest/slackbot.py
