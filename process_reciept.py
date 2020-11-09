from pprint import pprint
import glob
import json
import shutil
import os

try:
    os.mkdir("/home/oadetiba/workbench/pythonLAB/cloudguru/python/processed")
except OSError:
    pprint("'processed' directory already exists")
    
reciepts = glob.glob("/home/oadetiba/workbench/pythonLAB/cloudguru/python/new/reciept-[0-9]*.json")
subtotal = 0.0

for path in reciepts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['values'])
    name = path.split("/")[-1]
    #pprint(name)
    destination = f"/home/oadetiba/workbench/pythonLAB/cloudguru/python/processed/{name}"
    shutil.move(path, destination)
    pprint(f"moved '{path}' to '{destination}'")
    
pprint("Receipt subtotal: $%.2f" % subtotal)
    
        

