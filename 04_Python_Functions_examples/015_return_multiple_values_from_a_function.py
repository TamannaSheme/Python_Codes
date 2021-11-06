# Example 1: Return values using comma

def name():
    return "Arthur","Ethan","Peter"

# print the tuple with the returned values
print(name())

# get the individual items
name_1, name_2, name_3 = name()
print(name_1, name_2, name_3)
