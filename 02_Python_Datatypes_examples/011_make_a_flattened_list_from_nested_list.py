# Example 1: Using List Comprehension

my_list = [[7], [6, 5], [4, 3, 2, 1]]

flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)
