#!/usr/bin/python3
"""SUBREDDIT SUBSCRIBERS"""
import requests


def number_of_subscribers(subreddit):
    """Function to retrieve the number of subscribers for a given subreddit"""

    if not subreddit or not isinstance(subreddit, str):
        return 0

    try:
        r = requests.get('http://reddit.com/r/{}/about.json'.
                         format(subreddit),
                         headers={'User-Agent': 'mycoolapp/1.0'})
        r.raise_for_status()
        data = r.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    except requests.RequestException as e:
        return 0
