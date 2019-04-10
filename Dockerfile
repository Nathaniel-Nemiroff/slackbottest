RUN chmod +x exportscript
RUN ./exportscript

FROM ruby:2.5
RUN bash --version
RUN ./exportscript

FROM python:2.7-slim
RUN bash --version
RUN ./exportscript

FROM bash:4.4
RUN bash --version
RUN ./exportscript
