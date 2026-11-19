"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object

print(f'Status code is {response.status_code}')


if '200' in str(response):
    print(response.json())      # response object, json() method
else:
    print(f'Response failed, it has status code {response.status_code}')