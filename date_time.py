#!/usr/bin/env python3
""" DateTime """
from datetime import date
from datetime import datetime

def main():
    """ DATETIME OBJECTS """
    #Get today's date from datetime class
    today = datetime.now()
    print(today)
    # Get the current time
    _t = datetime.time(datetime.now())
    print("The current time is %s" % _t)
    #weekday returns 0 (monday) through 6 (sunday)
    wd_ = date.weekday(today)
    #Days start at 0 for monday
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    print("Today is day number %d" % wd_)
    print("which is a " + days[wd_])
    now = datetime.now() #get the current date and time
    #%c - local date and time, %x-local's date, %X- local's time
    print(now.strftime("%c"))
    print(now.strftime("%x"))
    print(now.strftime("%X"))
    print(now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM
    print(now.strftime("%H:%M")) # 24-Hour:Minute

if __name__ == "__main__":
    main()
