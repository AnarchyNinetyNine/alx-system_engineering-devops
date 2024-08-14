#!/usr/bin/python3

"""
    Function to query subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):

    """Return the total number of subscribers on a given subreddit."""

    CLIENT_ID = "8T_hvDU-VQ9UhrEtEhG4nw"
    SECRET_KEY = "J2jaV-I742YrkXTMGzQ6S6MjrTtHCQ"

    base_url = 'https://www.reddit.com/'
    data = {
                'grant_type': 'password',
                'username': 'Big_Confection_4617',
                'password': 'ArtukBay2019!'
            }

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    r = requests.post(
            base_url + 'api/v1/access_token',
            data=data,
            headers={'user-agent': 'my_app by Big_Confection_4617'},
            auth=auth)

    d = r.json()

    base_url = 'https://oauth.reddit.com'
    token = 'bearer ' + d['access_token']
    headers = {
            'Authorization': token,
            'User-Agent': 'my_app by Big_Confection_4617'}
    response = requests.get(
            base_url + "/r/{}/about.json".format(subreddit),
            headers=headers,
            allow_redirects=False)

    if response.status_code != 404:
        return response.json().get('data').get('subscribers')
    else:
        return 0
