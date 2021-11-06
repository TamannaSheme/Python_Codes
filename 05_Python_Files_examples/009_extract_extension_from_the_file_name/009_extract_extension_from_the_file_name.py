# Example 1: Using splitext() method from os module

import os
file_details = os.path.splitext('vaccine_data.txt') # path ('/path/file.ext')
print(file_details)
print(file_details[1])


# Example 2: Using pathlib module

import pathlib
print(pathlib.Path('vaccine_data.txt').suffix) # path ('/path/file.ext')
