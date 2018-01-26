## Combine both google_commander and toggl_commander
from google_commander import core as gcore
from toggl_commander import core as tgcore
import argparse
import json

# This is only went we are on interactive mode

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
