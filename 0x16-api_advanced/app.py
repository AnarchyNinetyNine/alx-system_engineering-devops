#!/usr/bin/python3

CLIENT_ID = "8T_hvDU-VQ9UhrEtEhG4nw"
SECRET_KEY = "J2jaV-I742YrkXTMGzQ6S6MjrTtHCQ"

import requests
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': 'Big_Confection_4617', 'password': 'ArtukBay2019!'}
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'my_app by Big_Confection_4617'},
		  auth=auth)
d = r.json()

token = 'bearer ' + d['access_token']

base_url = 'https://oauth.reddit.com'

headers = {'Authorization': token, 'User-Agent': 'my_app by Big_Confection_4617'}
response = requests.get(base_url + '/r/programming/about.json', headers=headers)

if response.status_code == 200:
    print(response.json().get('data').get('subscribers'))

print(token)
