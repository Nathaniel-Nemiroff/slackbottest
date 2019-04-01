FROM ubuntu
RUN ruby sina.rb \
	ngrok http 4567 \
