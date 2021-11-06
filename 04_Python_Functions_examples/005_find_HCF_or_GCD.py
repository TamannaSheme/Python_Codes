# Example 1: program to find H.C.F of two numbers using Loops

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 64 
num2 = 24

print("The H.C.F. of", num1, "and", num2,  "is:", compute_hcf(num1, num2))
