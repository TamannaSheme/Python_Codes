# Example 1: Using os module

import os

# file name with extension
file_name = os.path.basename('vaccine_data.txt') # path ('/path/file.ext')

# file name without extension
print(os.path.splitext(file_name)[0])


# Example 2:

import os

print(os.path.splitext('vaccine_data.txt')) # path ('/path/file.ext')


# Example 3: Using Path module

from pathlib import Path

print(Path('vaccine_data.txt').stem) # path ('/path/file.ext')
