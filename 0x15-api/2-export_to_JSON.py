#!/usr/bin/python3
"""API GET REQUEST"""
import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(f'{url}users/{sys.argv[1]}').json().get("username")
    todos = requests.get(f'{url}todos/', params={'userId': sys.argv[1]}).json()
    data = {sys.argv[1]: [{"task": t.get("title"), "completed": t.get("completed"), "username": user} for t in todos]}
    filename = f"{sys.argv[1]}.json"

    with open(filename, 'w') as f:
        json.dump(data, f)
