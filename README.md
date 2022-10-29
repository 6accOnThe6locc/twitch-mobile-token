## How to generate a token with mobile client_id (kd1unb4b3q4t58fwlpcbzcbnm76a8fp)

Antes de tudo defina as variaveis do script [login.py]()

Open Twitch login page in incognito tab **[here](https://www.twitch.tv/login)** then open the [DevTools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) 

## If everything is ok you will have something like this on your screen
![](https://imgur.com/To2Oiu5.png)


After opening click on the "Network" tab then try to login normally


Then you will arrive at this screen
![](https://imgur.com/DCmsSni.png)


Now you will right click on the URL https://passport.twitch.tv/protected_login and the option Block Request URL will appear click on it

![](https://imgur.com/YztrhMw.png)

If it works, the "Network request blocking" tab will appear
![](https://imgur.com/yzrZlBa.png)



Now you need to be quick. You will try to login but as the URL is blocked it will give an error, so you go to the payload tab and copy the "integrity_token" value edit the script run the login.py script


![](https://imgur.com/nWEMVlS.png)
