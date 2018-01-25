## Combine both google_commander and toggl_commander
from google_commander import core as gcore
from toggl_commander import core as tgcore
import argparse
import cmd
import json

# This is only went we are on interactive mode

class Command(cmd.Cmd):
    """ Lazzy toggle enhanced with gmail """

    ruler = '-'
    prompt = 'lazzy_cmd: '
    tickets = {}

    def do_l(self, wkrange=None, idx=None):
        if wkrange is None:
            wkrange = 'current'
        if idx is None:
            idx = 1
        self.tickets = json.dumps(gcore.GmailCommander().getmytickets(wk=wkrange, wkidx=idx), indent=4)
        print self.tickets
    
    def do_search(self, ticketid):
        self.search_ticket(ticketid)

    @staticmethod
    def search_ticket(self, ticketid):
        if ticketid is not None:
            for ticket in self.tickets:
                print ticket

if __name__ == '__main__':
    Command().cmdloop()