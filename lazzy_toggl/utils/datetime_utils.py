from time import localtime
from datetime import date, datetime, timedelta

def week_range(_wk=None, _idx=1):

    today = date.today()
    detailed_today = localtime()
    wkday = localtime()[6]
    start_nday_ago = abs(today.day - wkday - 2)
    s_date_delta = today - timedelta(days=start_nday_ago)
    wk_rg = week_range_delta(s_date_delta,wk=_wk, idx=_idx)

    return '%s %s' %(starting_date(wk_rg.get('st_date','')), end_date(wk_rg.get('ed_date','')))

def week_range_delta(init_range, wk=None, idx = None):
    wk_rg = {}
    # wk -> current
    if wk == 'last':
        s_date_delta = init_range - timedelta(days= 7 * idx)
        print s_date_delta
    e_date_delta =  s_date_delta + timedelta(days=6)
    wk_rg['st_date'] = date(s_date_delta.year, s_date_delta.month, s_date_delta.day)
    wk_rg['ed_date'] = date(e_date_delta.year, e_date_delta.month, e_date_delta.day)
    return wk_rg


def fdate(d):
    return d.strftime('%Y/%m/%d')

def starting_date(d):
    return 'after:%s' %(fdate(d))

def end_date(d):
    return 'before:%s' %(fdate(d))

def hours_to_seconds():
    return