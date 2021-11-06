# Example 1: Display the powers of 2 using anonymous function

terms = 11

# Uncomment code below to take input from the user
# terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
    print("Value of 2 to power",i,"is:",result[i])
