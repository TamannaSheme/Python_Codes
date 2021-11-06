# Example 1: Using float()

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isfloat('s66'))
print(isfloat('9.639'))
