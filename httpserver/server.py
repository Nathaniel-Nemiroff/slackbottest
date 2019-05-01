#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
import os
import time
import re
from slackclient import SlackClient

import logging
logging.basicConfig()
import requests

slack_client = SlackClient('xoxb-427109083139-595081416243-FI4yNZVWnXVt5A3T1P7kO4Jg')
slackbot_id = None

def sendMsg(msg):
    if slack_client.rtm_connect(with_team_state=False):
        print("nemi bot connected and running.")
        slackbot_id = slack_client.api_call("auth.test")["user_id"]
        slack_client.api_call(
            "chat.postMessage",
            channel='#botchannel',
            text=msg
            )

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print 'asdf'
        sendMsg('from simple http')
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):

        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length) 
        sendMsg(post_data)
        print post_data
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 80), Handler)

server.serve_forever()
