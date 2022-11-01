# Twitch: Simple script to get token with any Client Id

After many Twitch Miner users saying that the login method didn't work I implemented this method using [selenium-wire](https://pypi.org/project/selenium-wire/).
(headless mode not working [read more](https://github.com/ultrafunkamsterdam/undetected-chromedriver/issues/589))

# How to use
You will need [Chrome](https://www.google.com/chrome/) installed on your computer and download [Chrome WebDriver](https://chromedriver.chromium.org/downloads), both must be in the same version. 

Note: You can modify it to support other browsers but I won't teach it here.

## Installing dependencies
#### Linux
```bash
$ python3 -m pip3 install -r requirements.txt
```
#### Windows
```
python -m pip install -r requirements.txt
```
## Usage
Note: When you run the script it will ask for your password and your username, then it will open the browser and enter your username and password. You will need to manually enter your verification code. Wait a bit and hit enter on your console.

#### Linux
```bash
$ python3 main.py
```
#### Windows
```
python main.py
```

# Problems and Contact
Any problem open an issue or contact me on Discord (**Rafael Morais#9853**) or [Twitter](https://twitter.com/300Kled)
