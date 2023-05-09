#!/usr/bin/python3

"""Returns the top 10 posts in a subreddit"""

import requests


def top_ten(subreddit):
    """The function checks a subreddit and returns subscribed users"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    data = response.json().get('data')

    if data is None:
        return (0)

    posts = data.get('children')

    if response.status_code == 200:
        for post in posts[:10]:
            print(post.get('data').get('title'))
    else:
        return (0)
