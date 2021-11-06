# Example 1: print binary number using recursion

def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2,end = '')

# decimal number
dec = 47

convertToBinary(dec)
print(" is a Binary equivalent to Decimal of", dec)
