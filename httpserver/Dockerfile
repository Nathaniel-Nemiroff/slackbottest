FROM python:2.7
RUN pip install slackclient

#RUN curl -Lo /ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip;unzip -o /ngrok.zip -d ./
#RUN  ./ngrok authtoken 2BRrdymMATW3q4B8keykC_5PvpojiLFyeUDoS86Cvqa


WORKDIR /server
COPY . /server

EXPOSE 80
#EXPOSE 4040
ENV NAME ab

#CMD ["ngrok","http", "4567", "&"]
#CMD ["curl", "localhost:4040/api/tunnels"]
RUN echo '';echo '-----------------------';echo 'REMEMBER TO:';echo ' 1: Ensure your slackclient token is correct'; echo ' 2: expose 8000 to the world';echo '-----------------------';echo ''
CMD ["python", "server.py"]
