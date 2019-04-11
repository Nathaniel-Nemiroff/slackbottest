FROM bash:4.4

RUN  git clone https://github.com/Nathaniel-Nemiroff/slackbottest

RUN  ./slackbottest/exportscript
