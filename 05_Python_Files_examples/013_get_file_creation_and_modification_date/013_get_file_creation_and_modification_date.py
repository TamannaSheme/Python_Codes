# Example 1: Using os module

import os.path, time
#import sys,os
import pathlib


file = pathlib.Path('Digital_Clock.py')
print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))


# Example 2: Using stat() method

import datetime
import pathlib

fname = pathlib.Path('Digital_Clock.py')
print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))



