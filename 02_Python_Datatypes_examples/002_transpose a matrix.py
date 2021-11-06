# Example 1: transpose a matrix using a nested loop

X = [[12,9],
    [7 ,3],
    [5 ,6]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)
