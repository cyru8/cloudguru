#/usr/bin/env python3

import sys
import argparse

#build the parser
#parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description= "Read a file in the reverse")
parser.add_argument("filename", help="the file to read")
parser.add_argument("--limit", "-l", type=int, help="The number of lines to read")
parser.add_argument("--version", "-v", action="version", version="%(prog)s 1.0")
                    
args = parser.parse_args()
#print(args)

# parse the arguments
# read the file, reverse the content and print
with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()
    
    if args.limit:
        lines = lines[:args.limit]
        
    for line in lines:
        print(line.strip()[::-1])
