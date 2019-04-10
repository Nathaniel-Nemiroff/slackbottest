FROM ruby:2.5
RUN curl -Lo /ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip; unzip -o /ngrok.zip -d ./; ./ngrok --version

RUN ls;ls home
RUN ls;cat ./sina.rb
RUN ruby ./sina.rb
