FROM ruby:2.5
RUN echo 'NUMBER 0'
RUN curl -Lo /ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip; unzip -o /ngrok.zip -d ./
RUN git clone https://github.com/Nathaniel-Nemiroff/slackbottest
RUN  ./ngrok authtoken 2BRrdymMATW3q4B8keykC_5PvpojiLFyeUDoS86Cvqa
EXPOSE 4567
EXPOSE 4040
EXPOSE 80
RUN ./ngrok http -subdomain=nemiroffslackbot 4567 &
#http://nemiroffslackbot.ngrok.io
# RUN curl localhost:4040/api/tunnels

RUN export SLACK_BOT_TOKEN='xoxb-573900660641-580144662512-3Q5SHTLWCvyUPjgau3BVn1yy'

RUN gem install rubypython; gem install sinatra
RUN ruby ./slackbottest/sina.rb
RUN echo 'AFTER SINA....FAILED


