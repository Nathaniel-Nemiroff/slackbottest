from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

import io
from slackclient import SlackClient

import logging
logging.basicConfig()
import requests
import time

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly','https://www.googleapis.com/auth/drive']


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
                                    

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    
    #flow = InstalledAppFlow.from_client_secrets_file(
    #    'credentials.json', SCOPES)
    #creds = flow.run_local_server()
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    #results = service.files().list(
    #    pageSize=10, fields="nextPageToken, files(id, name)").execute()
    #items = results.get('files', [])

    #if not items:
    #    print('No files found.')
    #else:
    #    print('Files:')
    #    for item in items:
    #        print(u'{0} ({1})'.format(item['name'], item['id']))

    file_id = [FILE]
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    #fh = io.FileIO('result','wb')
    #fh = io.StringIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))
    strfh = fh.getvalue()
    strind = strfh.find('success=')
    if strfh[strind+8:strind+12] == 'true':
        sendMsg('success')
    else:
        sendMsg('failure')

if __name__ == '__main__':
    while(True):
        main()
        time.sleep(3600)
