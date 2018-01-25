from time import localtime
from datetime import date


def week_range(wk, idx):
    
    today = date.today()
    detailed_today = localtime()
    wkday = localtime()[6]

    st_date = date(today.year, today.month, today.day - wkday - 1)
    ed_date = date(today.year, today.month, st_date.day + 6)

    if wk == 'last':
        # Defaul is last week, idx = 1.
        st_date = st_date.replace(day=st_date.day - 7 * idx)
        ed_date = st_date.replace(day=ed_date.day - 7 * idx)

    return '%s %s' %(starting_date(st_date), end_date(ed_date))

def fdate(d):
    return d.strftime('%Y/%m/%d')

def starting_date(d):
    return 'after:%s' %(fdate(d))

def end_date(d):
    return 'before:%s' %(fdate(d))

def hours_to_seconds():
    return