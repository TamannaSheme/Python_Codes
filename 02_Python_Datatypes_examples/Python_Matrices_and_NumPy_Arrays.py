# Let's see how to work with a nested list.

A = [[1, 3, 6, 12], 
    [-7, 8, 9, 0],
    [-5, 7, 12, 19]]

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = [];        # empty list
for row in A:
    column.append(row[2])   

print("3rd column =", column)
