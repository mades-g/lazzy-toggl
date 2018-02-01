from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import re

from utils import datetime_utils

flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Lazzy Toggl chilling with Gmail'

class GmailCommander:

    def __init__(self):
        self.credentials = self.get_credentials()

    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                    'gmail-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def getmytickets(self, wk, wkidx, user_id='me'):
        querystring =  '"%s assigned an issue to Eudes"' %(datetime_utils.week_range(wk=wk, idx=wkidx))
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)

        response = service.users().messages().list(userId=user_id,
                                                q=querystring).execute()
        ticketlist = []
        if 'messages' in response:
            ticketlist.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, q=querystring,
                                                pageToken=page_token).execute()
            ticketlist.extend(response['messages'])

        mytickets = []
        
        for msg in ticketlist:
            ticket = {}
            message = service.users().messages().get(userId=user_id, id=msg['id'], format='metadata', metadataHeaders=['Subject']).execute()
            # [JIRA] (LB-73) Deposit button next to account balance on mobile -
            filtered_string = re.search('^\[JIRA\]\s+?\W(?P<ticketid>\w+-\d+)\W\s+?(?P<title>.*)', message['payload']['headers'][0]['value'])
            ticket['msgid'] = msg['id']
            # LB-73
            ticket['ticketid'] = '[%s]'%(filtered_string.group('ticketid'))
            # Deposit button next to account balance on mobile
            ticket['title'] = filtered_string.group('title')
            mytickets.append(ticket)
        return mytickets