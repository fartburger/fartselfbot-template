## SETUP<br />
To setup the bot, you will need both the bot account's token and the bot account's ID.<br />
#### Getting the bot's token<br />
To get the token, first log in the your bot's account in chrome(or any browser that you can view request headers in).<br />
Press F12 to enter the **Network** tab of Chrome's developer tools<br />
Now, go to a text channel and start typing, but don't send the message. In the network tab you should see a row titled `typing`.<br />
![what you are looking for](https://i.imgur.com/k1GqlXp.png)<br />
Click on the row.<br />
Now, click on the **Headers** tab if you are not already viewing it, and scroll down to the **Request Headers** section.<br />
Find and copy the value for `authorization:`.<br />
Now that you have your bot's token, download the ZIP of this repo and extract it to wherever you want.<br />
Edit the file `zeenode/config.py` and replace the text `"ENTER TOKEN HERE"` with the token you just copied.<br />
Now, copy your bot's ID and go to the file `zeenode/events/on_message.py`<br />
Change the value of the variable `botid` on line 15 to your bot's ID (make sure to remove these: <>)<br /><br />

**That's it**<br />
To start the bot, run the wake.bat script and it should start up. <br />

