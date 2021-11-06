# Example 1: Using datetime module

from datetime import datetime

my_date_string = "Aug 9 2018 11:11AM"

datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)
