import os
import time
import re
from slackclient import SlackClient

import requests

#instantiate slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
#bot's user id in slack: value is assigned after bot starts up
slackbot_id = None

#constraints
RTM_READ_DELAY = 1 # 1 second delay before reading from rtm
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


if slack_client.rtm_connect(with_team_state=False):
    print("nemi bot connected and running.")
    slackbot_id = slack_client.api_call("auth.test")["user_id"]
    slack_client.api_call(
        "chat.postMessage",
        channel='#everyone',
        text='test'
        )


'''
def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from slack rtm api to find bot commands
        if a bot command is found, this function returns a tuple of command and channel
        if its not found, this function returns none, none
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_detect_mention(event["text"])
            if user_id == slackbot_id:
                return message, event["channel"]
    return None, None

def parse_detect_mention(message_text):
    """
        finds a direct mention in message text (from beginning)
        returns the user ID which was mentioned, if none is dectected, returns none
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    # execute bot command if it's none

    #default response is help text for user
    default_response = "Cannot parse command, try *{}*.".format(EXAMPLE_COMMAND)

    #finds and executes given command
    response = None
    #this is where you implement more commands...
    if command.startswith(EXAMPLE_COMMAND):
        response = requests.get("http://api.open-notify.org/iss-now.json")

        #print(response.status_code)
        response="example recieved...*{}*.".format(response.status_code)

    #sends response back to channel
    slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response or default_response
            )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("nemi bot connected and running.")
        #read bot's id by calling api method auth.test
        slackbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command,channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed.  Exception traceback printed above.")
'''
