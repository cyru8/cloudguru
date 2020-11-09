import random
import json
import os

count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip() for word in open("/usr/share/dict/words").readlines()]

for objectID in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        "topic": random.choice(words),
        "values": "%.2f" % amount
    }
    with open(f"/home/oadetiba/workbench/pythonLAB/cloudguru/python/new/reciept-{objectID}.json", "w") as f:
        json.dump(content, f)


