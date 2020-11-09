#!/usr/bin/env python3

from pprint import pprint
#from time import localtime, mktime, strftime
import time

start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")

# Wait for user to stop time
input("Press 'Enter' button to stop timer ")

stop_time = time.localtime()

diff = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {diff} seconds")


#now = time.localtime()
#print(now, sep="")
#print(now.tm_hour)
