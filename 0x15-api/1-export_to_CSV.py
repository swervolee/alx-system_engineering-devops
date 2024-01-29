#!/usr/bin/python3
"""API GET REQUEST"""
import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(f'{url}users/{sys.argv[1]}').json().get("username")
    todos = requests.get(f'{url}todos/', params={'userId': sys.argv[1]}).json()
    data = [[t.get("userId"), user,
             t.get("completed"), t.get("title")] for t in todos]

    filename = f"{sys.argv[1]}.csv"
    with open(filename, 'w') as f:
        csvwriter = csv.writer(f, delimiter=",",
                               quotechar='"', quoting=csv.QUOTE_ALL)
        csvwriter.writerows(data)
