FROM python:2.7

EXPOSE 8000
#RUN server.py
CMD ['python', 'server.py']
