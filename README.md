# controller_bot

Bot to use as a terminal for your computer when this is on. It can be useful to control a Raspbery Pi from the phone without programs or static IPs.

## How it works

First of all, you must create your own Telegram bot and look for your Telegram User Id.

#### Getting your token

To get a token for a new Telegram Bot, in Telegram look for the [@BotFather](https://t.me/BotFather) and create a new one with the command '/newbot' then just follow the instructions and you will get a token (`YourTokenId`).

#### Getting your user id

Look for the bot [https://t.me/JsonDumpBot](@JsonDumpBot) , and you will receive a message that will include the parameter "```message"{"chat":{"id"}}```". This number is you user id (`YourUserId`).

After getting these items, create a file `ids.py` and add the lines:

```python3
userId = YourUserId # This DOES NOT NEED quotation marks
tokenId =  "YourTokenId" # This needs the quotation marks 
```
And save it in the same folder as the project. Now you can run it. 
If something fails, you can contact me throught my [Twitter](https://twitter.com/iam_agf).

## Taking advantage in a Raspberry Pi (or any computer).

First create a folder called `.controller` in your folder `/home/YOUR-USER-DIRECTORY`. Now run the command `sudo nano /etc/systemd/system/controller.service` and write in it

```
[Unit]
Description=Telegram Terminal Bot
Wants=network-online.target
After=network.target network-online.target
StartLimitIntervalSec=0

[Service]
Type=idle
WorkingDirectory=/home/YOUR-USER-DIRECTORY
ExecStart=/usr/bin/python3 /home/YOUR-USER-DIRECTORY/.controller/main.py
Restart=on-failure
RestartSec=3s

[Install]
WantedBy=multi-user.target

```

Then save it. Now type in the terminal

```
sudo -m pip install pyTelegramBotAPI
```
Because probably you ran this program in your user, not as the sudo user, and you need to install it this way to be able to use the program correctly as a daemon. After it, now run in the terminal 
```
systemctl enable controller
systemctl daemon-reload
```

Finally reboot your computer and you will be able to run this in your Telegram bot.

Notice that this will only work if you're connecting to a network already registered in your computer. If not, the `systemd` program will continue trying to conncet until it achieves it.

