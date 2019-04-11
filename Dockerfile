FROM ubuntu:18.04
RUN curl -Lo /ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip; unzip -o /ngrok.zip -d ./
RUN  ./ngrok authtoken 2BRrdymMATW3q4B8keykC_5PvpojiLFyeUDoS86Cvqa
RUN ./ngrok http 4567 &
RUN curl localhost:4040/api/tunnels


