""" Allows output calendars and provides calendar functionality, related to both time and datetime modules"""

# not Monday's are first day of week by default, unless changed calendar.setfirstweekday()
# uses current Gregorian calendar for past and future

import calendar

def b_DAY(year, month, day):
    # prints the day of the week someone was born on
    day_index = calendar.weekday(year, month, day)
    print(calendar.day_name[day_index])

def thurs_in_nov(year): 
    # returns the number of thursdays for november in a given year (data for Thanksgiving/shopping)
    # note months indexed(ie start at 0)
    
    thurs_count = 0
    c = calendar.Calendar()
    days = c.itermonthdays2(year=year, month=11) # return a iterator of tuples
    for day in days:
        if day[1] == 3:
            thurs_count += 1
    return thurs_count
    """ Better OPTION
    thurs_count = [day for day in calendar.monthcalendar(year, 11) if day[3] != 0]
    return len(thurs_count)
    """

def display_november(year):
    # simple calendar display of my favorite month
    c = calendar.TextCalendar()
    november = c.formatmonth(year, 11)
    print(november)

def html_display_month_calendar(year, month_number):
    # prints out calendar in html format, not too exciting but functional (view with open nov_cal.html)
    c = calendar.HTMLCalendar()
    nov_cal_display_code = c.formatmonth(year, month_number)
    print(nov_cal_display_code)



if __name__ == "__main__":
    b_DAY(1974, 11, 14)
    print(thurs_in_nov(2018))
    display_november(2018)
    html_display_month_calendar(2018, 11)