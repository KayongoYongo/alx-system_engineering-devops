#!/usr/bin/python3
""" Returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """The function checks a subreddit and returns subscribed users"""

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={'User-Agent': 'MyAPI/0.0.1'},
        allow_redirects=False)

    data = response.json().get("data")

    if data is None:
        return (0)

    count = data.get("subscribers")

    if response.status_code == 200:
        return (count)
    else:
        return (0)
