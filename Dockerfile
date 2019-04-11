FROM ubuntu:18.04

RUN  git clone https://github.com/Nathaniel-Nemiroff/slackbottest

RUN  ./slackbottest/exportscript
