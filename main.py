from random import choices
from uuid import uuid1

from requests import Session


LOGIN_URL = 'https://passport.twitch.tv/login'
CLIENT_ID = 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp'


def random_hex_chars(k) -> str:
    return ''.join(choices('0123456789abcdef', k=k))


class TwitchLogin:
    def __init__(self):
        self.session = Session()
        self.session.headers = {
            'accept': 'application/vnd.twitchtv.v3+json',
            'accept-encoding': 'gzip',
            'accept-language': 'en-US',
            'client-id': CLIENT_ID,
            'content-type': 'application/json; charset=UTF-8',
            'host': 'passport.twitch.tv',
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G975N Build/N2G48C) tv.twitch.android.app/13.4.1/1304010',
            'x-device-id': random_hex_chars(32),
        }

    def login(self, username, password):
        login_payload = {
            'client_id': CLIENT_ID,
            'force_twitchguard': False,
            'password': password,
            'undelete_user': False,
            'username': username,
        }
        while True:
            response = self.session.post(LOGIN_URL, json=login_payload)
            response_json = response.json()
            if 'captcha_proof' in response_json:
                login_payload['captcha'] = {
                    'proof': response_json['captcha_proof']
                }
            if 'error_description' in response_json:
                error_code = response_json['error_code']
                print(response_json['error_description'])
                if error_code == 3022:
                    login_payload['twitchguard_code'] = input(
                        'Twitch Code: '
                    ).strip()
                    continue
                elif error_code in [3001, 3003]:
                    exit()
                elif error_code == 1000:
                    exit('Wait some time to try again.')

            if 'access_token' in response_json:
                print('Token ->', response.json()['access_token'])
                break


def main():
    username = str(input('Username: ')).strip()
    password = str(input('Password: ')).strip()
    TwitchLogin().login(username, password)


if __name__ == '__main__':
    main()
