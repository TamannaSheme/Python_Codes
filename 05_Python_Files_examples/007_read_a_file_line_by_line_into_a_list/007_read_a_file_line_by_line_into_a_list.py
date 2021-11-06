# Example 1: 

#with open("vaccine_data.csv") as f:
with open("vaccine_data.txt") as f:
    content_list = f.readlines()

# print the list
print(content_list, "\n")

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)


# Example 2: Using for loop and list comprehension

#with open("vaccine_data.csv") as f:
with open("vaccine_data.txt") as f:
    content_list = [line for line in f]

print(content_list, "\n")

# removing the characters
#with open("vaccine_data.csv") as f:
with open("vaccine_data.txt") as f:
    content_list = [line.rstrip() for line in f]

print(content_list)
