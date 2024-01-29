#!/usr/bin/python3
"""API GET REQUEST"""
import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(f'{url}users/').json()
    todos = requests.get(f'{url}todos/').json()
    data = {}

    for i in users:
        data[i.get("id")] = [{"username": i.get("username"),
                              "task": t.get("title"), "completed": t.
                              get("completed")} for t in todos if t.
                             get("userId") == i.get('id')]

    filename = "todo_all_employees.json"

    with open(filename, 'w') as f:
        json.dump(data, f)
