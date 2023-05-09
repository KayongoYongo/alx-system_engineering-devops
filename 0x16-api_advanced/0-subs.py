#!/usr/bin/python3
""" Returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """The function checks a subreddit and returns subscribed users"""
    try:
        response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers={'User-Agent': 'MyAPI/0.0.1'})

        subreddit_data = response.json()['data']

        subreddit_subscriber_count = subreddit_data['subscribers']

        return (subreddit_subscriber_count)

    except KeyError:
        return (0)
