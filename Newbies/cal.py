#!/usr/bin/env python3
"""Calendar example."""
import calendar
# Create a plain text calendar
CAL = calendar.TextCalendar(calendar.MONDAY)
CAL_STR = CAL.formatmonth(2020, 1, 0, 0)
print(CAL_STR)

# Create an HTML formatted calendar
HC = calendar.HTMLCalendar(calendar.MONDAY)
HC_STR = HC.formatmonth(2020, 1)
print(HC_STR)

# loop over the days of a month
# zeroes indicate that the day of
# the week is in a next month or overlapping month
for i in CAL.itermonthdays(2020, 1):
    print(i)

# The calendar can give info based on locale
# such as names of days and months
# (full and abbreviated forms)
for name in calendar.month_name:
    print(name)
for day in calendar.day_name:
    print(day)

# calculate days based on a rule: For instance an audit day on the second Monday of every month
# Figure out what days that would be for each month, we can use the script
# as shown here

for month in range(1, 13):
    # It retrieves a list of weeks that represent the month
    mycal = calendar.monthcalendar(2020, month)
    # The first MONDAY has to be within the first two weeks
    week1 = mycal[1]
    week2 = mycal[2]
    if week1[calendar.MONDAY] != 0:
        auditday = week1[calendar.MONDAY]
    else:
        # if the first MONDAY isn't in the first week, it must be in the second
        # week
        auditday = week2[calendar.MONDAY]
    print("%10s %2d" % (calendar.month_name[month], auditday))
