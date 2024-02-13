#!/usr/bin/python3
"""Counts number of subs"""
import requests

def number_of_subscribers(subreddit=None):
    """Function to retrieve the number of subscribers for a given subreddit"""

    if not subreddit or not isinstance(subreddit, str):
        return 0

    try:
        r = requests.get('http://reddit.com/r/{}/about.json'.format(subreddit), headers={'User-Agent': 'mycoolapp/1.0'},
                         allow_redirects=False)
        r.raise_for_status()  # Raise an exception for bad status codes (e.g., 404)
        data = r.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    except requests.RequestException as e:
        print("Error:", e)
        return 0
