import os, requests
import sys
import json
import re
class TogglCommander:
    # Since Projects Time entries have almost the same call signature in the future should be rethinked o.o

    project_entry = {
        "project": {
            "name": "", # Description from time entry
            "wid": "",
            "is_private": False,
            "cid": ""
            }
    }

    # e.g
    '''
        tickets[ticketid] + tickets[title] -> descripition
    '''
    time_entry = {
        "time_entry": {
            "wid": "",
            "pid": "",
            "tag": "[]",
            "start": "",
            "duration": "",
            "created_with":"lazzy_toggl",
            "description": ""
        }
    }

    def __init__(self):
        try:
            self.toggl_api_key  = os.environ['TOGGL_API_KEY']
        except:
            print "Lazzy nuff to provide TOGGL_API key..sad"
            sys.exit(0)
        #test
        data = json.load(open('/home/v4let3/lazzy-toggl/toggl_data.json'))['data']
        toggl_projects = data.get('projects')#tg_cmd.my_toggl_info.get('projects')
        toggl_clients = data.get('clients')#tg_cmd.my_toggl_info.get('clients')
        self.api_url = 'https://www.toggl.com/api/v8/'
        self.time_entry_path = 'time_entries'
        self.project_entry_path = 'projects'
        self.auth = (self.toggl_api_key, 'api_token')
        self.my_toggl_info = data #requests.get('%s%s' %(self.api_url,'me?with_related_data=true'), auth=self.auth).json()

    # Time entries

    def create_time_entry(self, entry, wid=2408938, pid=""):
        print '%s%s' %(self.api_url,self.time_entry_path)
        entry['wid'] = wid
        entry['pid'] = pid
        _entry = self.time_entry['time_entry'].copy()
        _entry.update(entry)
        print _entry
    def stop_time_entry(self, entry_id):
        pass

    def update_time_entry(self, *args, **kargs):
        pass

    def delete_time_entry(self, entry_id=None):
        pass

    def get_time_entry(self):
        pass

    # Projects

    def create_project_entry(self):
        pass

    def get_project_entry(self, pid):
        pass

    def delete_project_entry(self, pid):
        pass


    @staticmethod
    def find_entry_pid(self, search_val):
        pass

    def find_client_id(self, search_val=None):
        if search_val is not None:
            clients = str(self.my_toggl_info.get('clients')).encode('utf-8') # get clients
            search_query = '%s.*?\W.*?(\d+)' %(search_val)
            search_result = re.search(search_query, clients, flags=2)
            if search_result is not None:
                client_id = search_result.group(0)
                self.project_entry['project']['cid'] = client_id
            else:
                print 'Unknown project.'
        else:
            print 'Empty Jira ticket ID.'