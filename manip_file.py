#!/usr/bin/env python3
street_file = open("street.txt", "r")
print(street_file)

street_read = street_file.read()

print(street_read, end=(""))

street_file.close()
#street_seek = street_file.seek()
#print(street_seek)


