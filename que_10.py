# Q10. Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'


from datetime import datetime, timedelta
def subtract_days(date, n):
    return (datetime.strptime(date, '%y-%m-%d') - timedelta(n)).date()

result = subtract_days('16-12-10', 11)
print(result) 