## Combine both google_commander and toggl_commander
from google_commander import core as gcore
from toggl_commander import core as tgcore
import argparse
import cmd
import sys
from utils import  data_types
import re

# This is only went we are on interactive mode

g_cmd = gcore.GmailCommander()
tg_cmd = tgcore.TogglCommander()

class Command(cmd.Cmd):

    tickets_list = {}
    prompt = "Lazy Toggl: "

    def do_list_tickets(self, line):
        if line == '':
            self.tickets_list = g_cmd.getmytickets()
        else:
            args = line.split()
            _wk = args[0]
            if len(args) == 2:
                _idx = line.split()[1][-1] #N=(n)
            else:
                _idx = 1
            self.tickets_list = g_cmd.getmytickets(wk=_wk, wkidx=_idx)
        print data_types.show_data(self.tickets_list)

    def complete_list_tickets(self, text, line, begidx, endidx):
        ''' List last N tickets '''
        return ['last N=']

    def complete_create_toggl_entry(self, text, line, begidx, endidx):
        search_list = list(
            map(lambda ticket:
                            re.search('\[(?P<ticketid>.*)\]',
                            ticket.get('ticketid')).group('ticketid')
            , self.tickets_list)
        )
        if not text:
            completions = search_list[:]
        else:
            completions = [ ticket_ref
                            for ticket_ref in search_list
                            if ticket_ref.startswith(text)
                            ]
        return completions

    def do_create_toggl_entry(self, line):
        print line
    
    def do_exit(self, line):
        return True


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-i':
        print 'Starting interactive mode'
        Command().cmdloop()
    else:
        print 'Going with argparse'
        main_parser = argparse.ArgumentParser(
                                            prog='lazzy toggl',
                                            usage=None,
                                            description='Lazzy Toggl enchaned with Gmail',
                                            epilog=None,
                                            version='1.0.0'
        )

        main_parser.add_argument('-l', default='current', nargs='+', help='List your tickets, default behaviour is the current one.', dest='list_tickets')

        argsv = main_parser.parse_args()

        print argsv.list_tickets
        print main_parser.get_default('list_tickets')

if __name__ == '__main__':
    main()
