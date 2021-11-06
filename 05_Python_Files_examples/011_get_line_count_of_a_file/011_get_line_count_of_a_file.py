# Example 1: Using a for loop

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print("Number of lines in a dataset:", file_len("vaccine_data.txt")) # path ('/path/file.ext')

# Example 2: Using list comprehension

num_of_lines = sum(1 for l in open('vaccine_data.txt')) # path ('/path/file.ext')

print("Number of lines in a dataset:", num_of_lines)
