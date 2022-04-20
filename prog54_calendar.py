import calendar
# this prints the calendar of the year 2018
# firstweekday represents the first weekday of every month
# ex: if firstweekday = 6 every month starts with sunday
# .formatyear(year, w, l, c) here :
# w = width, l = length, c = column length of calendar
print(calendar.TextCalendar(firstweekday=6).formatyear(2018))
# this prints a specific month of a year
print(calendar.TextCalendar(firstweekday=6).formatmonth(2018, 10))

# alternate way to print calendar of a year
print(calendar.calendar(2018, 2, 1, 6))

# .weekday(year, month, day) Returns the day of the week
# (0 is Monday) for year (1970–…), month (1–12), day (1–31)
week_num = calendar.weekday(2018, 10, 12)
print(week_num)

# this makes a list for all the weekdays as:
# lis = ['Monday', 'Tuesday', ......'Sunday']
lis = list(calendar.day_name)
print(lis)

# to get the name we can use the following
weekday_name = lis[calendar.weekday(2018, 10, 12)]
print(weekday_name)
