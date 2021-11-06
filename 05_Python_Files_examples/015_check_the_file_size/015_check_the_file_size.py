# Example 1: Using os module

import os

file_stat = os.stat('vaccine_data.txt')
print("The size of file is:", file_stat.st_size, "bytes.")


# Example 2: Using pathlib module

from pathlib import Path

file = Path('vaccine_data.txt')
print("The size of file is:", file.stat().st_size, "bytes.")
