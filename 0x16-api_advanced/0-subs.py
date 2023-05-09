#!/usr/bin/python3

"""Returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """The function checks a subreddit and returns subscribed users"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    data = response.json().get("data")

    if data is None:
        return (0)

    count = data.get("subscribers")

    if response.status_code == 200:
        return (count)
    else:
        return (0)
