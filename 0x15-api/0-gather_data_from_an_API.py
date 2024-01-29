#!/usr/bin/python3
"""API GET REQUEST"""
import requests
import sys


url = 'https://jsonplaceholder.typicode.com/'
user = requests.get(f'{url}users/{sys.argv[1]}').json().get("name")
todos = requests.get(f'{url}todos/', params={'userId': sys.argv[1]}).json()
completed = [i for i in todos if i.get("completed")]
print("Employee {} is done with tasks({}/{}):".
      format(user, len(completed), len(todos)))
[print("\t {}".format(i.get("title"))) for i in completed]
