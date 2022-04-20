from datetime import datetime

# strptime function is used to convert a string date format to
# a datetime format of-->
# datetime.strptime(timestamp, ‘%d/%m/%y %H:%M:%S’)

# IMPORTANT: time_format = '%a %d %b %Y %H:%M:%S %z'
# %z for timezone

# consider the time stamp in string format
# DD/MM/YY H:M:S.micros
time_data = "25/05/99 02:35:5.523"

# format the string in the given format :
# day/month/year hours/minutes/seconds-microseconds
format_data = "%d/%m/%y %H:%M:%S.%f"
# %d %m etc are abbreviation to connect string input to datetime
# format

# Using strptime with datetime we will format
# string into datetime
date = datetime.strptime(time_data, format_data)

# now we can individually access the hours, minute, seconds
print(date.min)

# full format of date
print(date)

# once string is converted to datetime format using strptime
# we can add and subtract time too !!
time_data2 = "25/05/99 02:38:8.023"
date2 = datetime.strptime(time_data2, format_data)
print(date2)
res = date2 - date
print(res.seconds)
