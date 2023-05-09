#!/usr/bin/python3

"""Returns the top 10 posts in a subreddit"""

import requests


def top_ten(subreddit):
    """The function return top 10 posts"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        posts =  response.json().get('data').get('children')

        if response.status_code == 200:
            for post in posts[:10]:
                print(post.get('data').get('title'))
    except Exception:
        print(None)
