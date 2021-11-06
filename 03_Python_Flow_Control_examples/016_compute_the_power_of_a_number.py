# Example 1: Calculate power of a number using a while loop

base = 2
exponent = 3
power = exponent

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Value of", base, "power", power, "is:", str(result))
