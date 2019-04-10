FROM ruby:2.5
RUN  git clone https://github.com/Nathaniel-Nemiroff/slackbottest

RUN  gem install rubypython; gem install sinatra
RUN  ruby ./slackbottest/sina.rb &
