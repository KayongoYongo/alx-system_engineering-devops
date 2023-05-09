#!/usr/bin/python3
""" Returns the number of subscribers"""

import requests

""" The below code has been commented out.
    I was looking for an alternative way of using the Reddit API.
    But with Authentication.
    If I comment it out, it still works
"""

"""`
CLIENT_ID = 'mEEAEnhSzXNMdP0oKZCNTA'
CLIENT_SECRET = 'hTeaC9qSBlpaeuqFgLWGabJqVAhbCw'

# Authenticate Reddit app
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

# here we pass our login method (password), username, and password
data = {'grant_type': 'client_credentials'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyAPI/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
"""


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
