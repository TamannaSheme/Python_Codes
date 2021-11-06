# Example 1: multiply two matrices using nested loops

# 3x3 matrix
X = [[12,9,3],
    [4,5,6],
    [7,8,3]]

# 3x4 matrix
Y = [[6,8,1,3],
    [5,7,3,4],
    [0,6,9,1]]

# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)
