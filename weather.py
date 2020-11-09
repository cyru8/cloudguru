
#!/usr/bin/env python3
# https://openweathermap.org/current#zip
# 5d3c6d62faf6d56387f503fd45ff49c0
# export OWM_API_KEY="5d3c6d62faf6d56387f503fd45ff49c0"

import os
from pprint import pprint
import requests
import sys

from argparse import ArgumentParser

parser = ArgumentParser(description="Geth the current weather information for your zipcode")
parser.add_argument("zip", help="zip/postal code to get weather for")
parser.add_argument("--country", default="us", help="country zip/postal belongs to, default is 'ca'")

args = parser.parse_args() 

api_key = os.getenv("OWM_API_KEY")

if not api_key:
    pprint("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res = requests.get(url)
#pprint(res)

if res.status_code != 200:
    print(f"Error talking to weaher provider: {res.status_code}")
    sys.exit(1)
pprint(res.json())