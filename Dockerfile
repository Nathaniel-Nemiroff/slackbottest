FROM ruby:2.5
RUN curl -Lo /ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip; unzip -o /ngrok.zip -d ./; ./ngrok --version
RUN git clone https://github.com/Nathaniel-Nemiroff/slackbottest

RUN gem install rubypython; gem install sinatra
RUN ruby ./slackbottest/sina.rb &
