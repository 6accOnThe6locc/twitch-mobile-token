import requests


USERNAME = '' # YOU USERNAME HERE
PASSWORD = '' # YOU PASSWORD HERE
USER_AGENT = '' # YOU USER AGENT HERE
INTEGRITY_TOKEN = '' # YOU INTEGRITY TOKEN
TWITCH_GUARD_CODE = '' # YOU TWITCH GUARD CODE HERE

headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://www.twitch.tv',
    'Referer': 'https://www.twitch.tv/',
    'User-Agent': USER_AGENT,
}

data = {
    'username': USERNAME,
    'password': PASSWORD,
    'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',
    'undelete_user': False,
    'integrity_token': ' integrity_token HERE',
    "twitchguard_code": ' YOUR TWITCH GUARD CODE HERE'
}

response = requests.post(
    'https://passport.twitch.tv/protected_login', headers=headers, json=data
)
print(response.json()['acess_token'])
