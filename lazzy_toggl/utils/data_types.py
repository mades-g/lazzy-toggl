import json
import sys

def show_data(data, type='json'):
    try:
        data_to_be_shown = json.dumps(data, indent=4)
    except RuntimeError:
        print "Invalid data type."
        sys.exit(0)
    print data_to_be_shown
