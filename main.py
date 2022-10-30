import json
from time import sleep

from undetected_chromedriver import ChromeOptions
from seleniumwire.undetected_chromedriver.v2 import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SLEEP_TIME = 10
EXECUTABLE_PATH = ''   # https://chromedriver.chromium.org/downloads
USERNAME = str(input('Username: ')).strip()
PASSWORD = str(input('Password: ')).strip()
CLIENT_ID = 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp'
HEADLESS = True


def get_chrome_options() -> ChromeOptions():
    options = ChromeOptions()
    if HEADLESS:
        options.add_argument('--headless')
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
        data['client_id'] = CLIENT_ID
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
    sleep(SLEEP_TIME)
    driver.execute_script(
        'document.querySelector("#root > div > div.scrollable-area > div.simplebar-scroll-content > div > div > div > div.Layout-sc-nxg1ff-0.gZaqky > form > div > div:nth-child(3) > button > div > div").click()'
    )


def send_verification_code(driver: Chrome):
    while True:
        code = str(input('Please enter the 6-digit code sent to your email: '))
        if len(code) != 6:
            print('Invalid Login Verification code entered, please try again.')
        else:
            break
    base_xpath = '/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[2]/div/div[{idx}]/div/input'
    for idx, numeric in enumerate(code, start=1):
        driver.find_element(By.XPATH, base_xpath.format(idx=idx)).send_keys(
            numeric
        )
    sleep(SLEEP_TIME)


def wait_browser_load(driver: Chrome):
    sleep(SLEEP_TIME)
    driver.get('https://www.twitch.tv/settings/profile')
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'display-name'))
    )


def main():
    driver = Chrome(
        options=get_chrome_options(), executable_path=EXECUTABLE_PATH
    )
    driver.request_interceptor = interceptor
    driver.get('https://twitch.tv/login')
    do_login(driver)
    send_verification_code(driver)
    wait_browser_load(driver)
    token = get_token(driver)
    print(f'token -> {token}')


if __name__ == '__main__':
    main()
