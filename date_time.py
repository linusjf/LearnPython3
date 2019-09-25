#!/usr/bin/env python3
""" DateTime """
from datetime import date
from datetime import datetime
from datetime import timedelta


def main():
    """ DATETIME OBJECTS """
    # Get today's date from datetime class
    today = datetime.now()
    print(today)
    # Get the current time
    _t = datetime.time(datetime.now())
    print("The current time is %s" % _t)
    # weekday returns 0 (monday) through 6 (sunday)
    wd_ = date.weekday(today)
    # Days start at 0 for monday
    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"]
    print("Today is day number %d" % wd_)
    print("which is a " + days[wd_])
    now = datetime.now()  # get the current date and time
    # %c - local date and time, %x-local's date, %X- local's time
    print(now.strftime("%c"))
    print(now.strftime("%x"))
    print(now.strftime("%X"))
    print(now.strftime("%I:%M:%S %p"))  # 12-Hour:Minute:Second:AM
    print(now.strftime("%H:%M"))  # 24-Hour:Minute

    # construct a basic timedelta and print it
    print(timedelta(days=365, hours=8, minutes=15))
    # print today's date
    print("today is: " + str(datetime.now()))
    # print today's date one year from now
    print("one year from now it will be: " +
          str(datetime.now() + timedelta(days=365)))
    # create a timedelta that uses more than one argument
    print("in one week and 4 days it will be " +
          str(datetime.now() + timedelta(weeks=1, days=4)))
    # How many days until New Year's Day?
    today = date.today()  # get todays date
    nyd = date(today.year, 1, 1)  # get New Year Day for the same year
    # use date comparison to see if New Year Day has already gone for this year
    # if it has, use the replace() function to get the date for next year
    if nyd < today:
        print(
            "Last New Year's was %d days ago." %
            ((today - nyd).days))

    # get coming New Year Day for the same year
    nextnyd = date(today.year + 1, 1, 1)

    if nextnyd > today:
        print(
            "Upcoming New Year's is in %d days." %
            ((nextnyd - today).days))


if __name__ == "__main__":
    main()
