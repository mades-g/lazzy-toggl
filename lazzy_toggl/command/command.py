import cmd
from google_commander import core
class Command(cmd.Cmd, core.GmailCommander):
    """
        Lazzy Toggl command-line
    """
    def __init__(self):
        pass
    def do_list_tickets(self, wk='current'):
        pass

if __name__ == '__main__':    