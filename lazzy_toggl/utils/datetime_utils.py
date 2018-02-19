from time import localtime
from datetime import date, datetime, timedelta
import sys
import re

def week_range(_wk=None, _idx=None):

    today = date.today()
    detailed_today = localtime()
    wkday = localtime()[6]
    start_nday_ago = abs(today.day + wkday - 2)
    s_date_delta = today - timedelta(days=start_nday_ago)
    wk_rg = week_range_delta(s_date_delta,wk=_wk, idx=_idx)
    print '%s %s' %(starting_date(wk_rg.get('st_date','')), end_date(wk_rg.get('ed_date','')))
    return '%s %s' %(starting_date(wk_rg.get('st_date','')), end_date(wk_rg.get('ed_date','')))

def week_range_delta(init_range, wk=None, idx = None):

    wk_rg = {}
    # wk -> current
    if wk == 'last':
        try:
            x_weeks_back = int(idx)
        except ValueError:
            print "Last argument must be a number."
            sys.exit(0)
        init_range = init_range - timedelta(days=(7 * x_weeks_back))
    e_date_delta =  init_range + timedelta(days=6)
    wk_rg['st_date'] = date(init_range.year, init_range.month, init_range.day)
    wk_rg['ed_date'] = date(e_date_delta.year, e_date_delta.month, e_date_delta.day)
    return wk_rg

def total_hours_minutes(hours_minutes):
    hours_index = hours_minutes.find('h')
    minutes_index = hours_minutes.find('m')
    total_seconds = 0
    minutes = 0
    hours = 0
    if hours_index > -1:
        hours = hours_minutes[0:hours_index]
        try:
            minutes = int(hours)
        except:
            print 'Invalid time.'
            sys.exit()
        if minutes_index > -1:
            minutes = hours_minutes[hours_index + 1:minutes_index] 
            try:
                minutes = int(minutes)
            except:
                print 'Invalid time.'
                sys.exit()
        else:
            re_helper = '$|(\d+)$'
            results = re.search(re_helper,hours_minutes).groups()
            if results[0] is not None:
                minutes = results[0]
            else:
                print 'Invalid time.'
                sys.exit()

    elif minutes_index > -1:
        minutes = hours_minutes[0:minutes_index]
    elif re.search('(^\d+)$',hours_minutes) is not None:
        total_seconds = int(re.search('(^\d+)$',hours_minutes).group(0))
        print 'Going with seconds'
    else:
        print 'Invalid time.'
        sys.exit()
    total_seconds += minutes_to_seconds(int(minutes))
    total_seconds += hours_to_seconds(int(hours))
    print 'Total seconds: ', total_seconds
    return total_seconds


def fdate(d):
    return d.strftime('%Y/%m/%d')

def starting_date(d):
    return 'after:%s' %(fdate(d))

def end_date(d):
    return 'before:%s' %(fdate(d))

def hours_to_seconds(duration):
    return duration * 3600

def minutes_to_seconds(duration):
    return duration * 60