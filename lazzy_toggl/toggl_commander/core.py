import os, requests

class TogglCommander:
    # Since Projects Time entries have almost the same call signature in the future should be rethinked o.o

    project_entry = {
        "project": {
            "name": "",
            "wid": "",
            "is_private": "",
            "cid": ""
            }
    }

    time_entry = {
        "time_entry": {
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
        self.api_url = 'https://www.toggl.com/api/v8/'
        self.time_entry_path = 'time_entries'
        self.project_entry_path = 'projects'
        self.auth = (self.toggl_api_key, 'api_token')

    # Time entries

    def create_time_entry(self, pid=None):
        pass

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

     # Tasks
