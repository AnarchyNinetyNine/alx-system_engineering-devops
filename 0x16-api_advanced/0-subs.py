#!/usr/bin/python3

"""
    This module provides a function to query the Reddit API
    and return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):

    """Returns the number of subscribers for a given subreddit."""

    headers = {'User-Agent': 'Custom'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
