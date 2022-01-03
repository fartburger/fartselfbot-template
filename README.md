##SETUP\n
To setup the bot, you will need both the bot account's token and the bot account's ID.\n
####Getting the bot's token\n
To get the token, first log in the your bot's account in chrome(or any browser that you can view request headers in).\n
Press F12 to enter the **Network** tab of Chrome's developer tools\n
Now, go to a text channel and start typing, but don't send the message. In the network tab you should see a row titled `typing`.\n
![what you are looking for](https://i.imgur.com/k1GqlXp.png)\n
Click on the row.\n
Now, click on the **Headers** tab if you are not already viewing it, and scroll down to the **Request Headers** section.\n
Find and copy the value for `authorization:`.\n
Now that you have your bot's token, download the ZIP of this repo and extract it to wherever you want.\n
Edit the file `zeenode/config.py` and replace the text `"ENTER TOKEN HERE"` with the token you just copied.\n
Now, copy your bot's ID and go to the file `zeenode/events/on_message.py`\n
Change the value of the variable `botid` on line 15 to your bot's ID (make sure to remove these: <>)\n\n

**That's it**\n
To start the bot, run the wake.bat script and it should start up. \n

