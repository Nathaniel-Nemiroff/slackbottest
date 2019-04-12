FROM ruby:2.5

RUN  git clone https://github.com/Nathaniel-Nemiroff/slackbottest
RUN  gem install rubypython; gem install sinatra
EXPOSE 4567
RUN  ruby ./slackbottest/sina.rb
RUN echo 'AFTER SINA'
#RUN curl localhost:4567
