#!/usr/bin/python3
"""Has one functin that gets top 10 hottest post from a reddit API"""
import requests
import sys


def top_ten(subreddit):
    """Gets top 10 hottests post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}
    headers = {'User-Agent': '0x16-api_advanced:project:\
    v1.0.0 (by /u/firdaus_cartoon_jr)'}

    if not subreddit or not isinstance(subreddit, str):
        print("None")
        sys.exit()

    try:
        r = requests.get(url,
                         params=params,
                         headers=headers)
        r.raise_for_status

        data = r.json().get("data")

        posts = data.get("children")
        titles = [post.get("data").get("title") for post in posts]
        [print(item) for item in titles]
    except Exception:
        print("None")
