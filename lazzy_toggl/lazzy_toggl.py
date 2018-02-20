## Combine both google_commander and toggl_commander
from google_commander import core as gcore
from toggl_commander import core as tgcore
import argparse
import cmd
import sys
from utils.data_types import  show_data
from utils.datetime_utils import total_hours_minutes
import re

# This is only went we are on interactive mode

g_cmd = gcore.GmailCommander()
tg_cmd = tgcore.TogglCommander()

class Command(cmd.Cmd):
    tickets_list = {}
    current_t = {}
    prompt = "Lazy Toggl: "
    error_log = []
    # Save this on file so there's no need to request it again
    def parseline(self, line):
        """Parse the line into a command name and a string containing
        the arguments.  Returns a tuple containing (command, args, line).
        'command' and 'args' may be None if the line couldn't be parsed.
        """
        line = line.strip()
        if not line:
            return None, None, line
        elif line[0] == '?':
            line = 'help ' + line[1:]
        elif line[0] == '!':
            if hasattr(self, 'do_shell'):
                line = 'shell ' + line[1:]
            else:
                return None, None, line
        i, n = 0, len(line)
        while i < n and line[i] in self.identchars: i = i+1
        cmd, arg = line[:i], line[i:].strip()
        return cmd, arg, line

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
        show_data(self.tickets_list)

    def complete_list_tickets(self, text, line, begidx, endidx):
        ''' List last N tickets '''
        list_tickets_opts = ['last N=']
        if not text:
            completions = list_tickets_opts[:]
        else:
            completions  = [ opts
                            for opts  in list_tickets_opts
                            if opts.startswith(text)
                            ]
        return completions

    def complete_create_toggl_entry(self, text, line, begidx, endidx):
        search_list = list(
            map(lambda ticket:
                            re.search('\[(?P<ticketid>.*)\]',
                            ticket.get('ticketid')).group('ticketid')
            , self.tickets_list)
        )
        if not text or text == '':
            completions = search_list[:]
        else:
            completions = [ ticket_ref
                            for ticket_ref in search_list
                            if ticket_ref.startswith(text)
                            ]
        return completions

    def do_create_toggl_entry(self, line): #-b bulk 
        entry = {}
        if line != '' or line != '--all':
            argsv = line.split()
            ticket_ref = re.search('(\A\w*)-|(\D.*)', line, flags=2) # bug for 21bet 188...
            if ticket_ref is not None:
                if ticket_ref.group(1) is None:
                    line = ticket_ref.group(0)
                else:
                    line =  ticket_ref.group(1)
                for ticket_ref in self.tickets_list:
                    search_query = '(%s_\d+)' %(line)
                    result = re.search(search_query, str(ticket_ref), flags=2)
                    if result is not None:
                        entry['description'] = ticket_ref[result.group(0)]['description']
                        break
                try:
                    start_idx = argsv.index('-s')
                    try:
                        start = argsv[start_idx + 1] # validate starting date
                        print start
                    except:
                        self.error_log.append('Empty starting time.')
                except:
                    print 'No starting time provided...falling for default.'

                try:
                    duration_idx = argsv.index('-d')
                    durantion = argsv[duration_idx + 1] # validate duration
                    entry['duration'] = total_hours_minutes(durantion)
                except:
                    print 'Invalid duration.'

                if len(self.error_log) == 0:
                    tg_cmd.create_time_entry(entry)
                else:
                    print self.error_log[0]

        else:
            print 'Invalid toggl entry.'

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
