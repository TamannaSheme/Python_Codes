# Example 1: display calendar of the given month and year

# importing calendar module
import calendar

yyyy = 2022  # year
mm = 1    # month  #'01' will give error

# To take month and year input from the user
# yyyy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yyyy, mm))
