#!/usr/bin/python3
"""This python script will fetch my headers"""

import requests

response = requests.get('http://httpbin.org/headers')

print(response.status_code)
print(response.text)
