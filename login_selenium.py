import json
from time import sleep

from undetected_chromedriver import ChromeOptions
from seleniumwire.undetected_chromedriver.v2 import Chrome
from selenium.webdriver.common.by import By


EXECUTABLE_PATH = 'PASTE CHROME DRIVER PATH HERE'   # https://chromedriver.chromium.org/downloads
USERNAME = str(input('Username: ')).strip()
PASSWORD = str(input('Password: ')).strip()


def get_chrome_options() -> ChromeOptions():
    options = ChromeOptions()
    options.add_argument('--log-level=3')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--lang=en')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    return options


def interceptor(request) -> str:
    if (
        request.method == 'POST'
        and request.url == 'https://passport.twitch.tv/protected_login'
    ):
        body = request.body.decode('utf-8')
        data = json.loads(body)
        data['client_id'] = 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp'
        request.body = json.dumps(data).encode('utf-8')
        del request.headers['Content-Length']
        request.headers['Content-Length'] = str(len(request.body))


def get_token(driver: Chrome) -> str:
    cookies = driver.get_cookies()
    for cookie in cookies:
        if cookie['name'] == 'auth-token':
            return cookie['value']


def do_login(driver: Chrome):
    driver.find_element(By.ID, 'login-username').send_keys(USERNAME)
    driver.find_element(By.ID, 'password-input').send_keys(PASSWORD)
    sleep(0.3)
    driver.execute_script(
        'document.querySelector("#root > div > div.scrollable-area > div.simplebar-scroll-content > div > div > div > div.Layout-sc-nxg1ff-0.gZaqky > form > div > div:nth-child(3) > button > div > div").click()'
    )


def main():
    driver = Chrome(
        options=get_chrome_options(), executable_path=EXECUTABLE_PATH
    )
    driver.request_interceptor = interceptor
    driver.get('https://twitch.tv/login')
    do_login(driver)
    print(
        'enter your verification code in the browser and wait for the twitch website to load.'
    )
    input('then press enter key in console')
    token = get_token(driver)
    print(f'token -> {token}')


if __name__ == '__main__':
    main()
