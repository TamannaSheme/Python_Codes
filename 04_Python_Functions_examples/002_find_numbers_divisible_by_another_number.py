# Example 1: 

# Take a list of numbers
my_list = [17, 34, 51, 43, 68, 72, 119, 327, 243, 986]

# use anonymous function to filter
result = list(filter(lambda x: (x % 17 == 0), my_list))

# display the result
print("Numbers divisible by 17 are",result)
