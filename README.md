# Reddit-to-Telegram-Python-Bot
Simple bot using [PRAW](https://github.com/praw-dev/praw) and [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (those modules do all the hard stuff). Minimal knowledge of python needed or just follow README.

## Background
Greetings! A few months ago I wrote some very basic code that allowed me to send my GF batches of cute pictures from Reddit. Everyone I told about this was interested so I thought I might as well put the code out their so I can save at least one person a few hours of reading the PRAW documentation and writing this.

## What does it do?
It essentially just aggregates an adjustable number of current top links from a selected subreddit and sends them to a selected telegram chat. It will ignore stickied or permanent posts.

## Prerequisites
Before working with the provided code first you need to have three things ready.
* Obtaining a [Reddit API key](https://www.reddit.com/wiki/api)
* Creating a [Telegram Bot](https://core.telegram.org/bots) and generating its [token](https://core.telegram.org/bots#generating-an-authorization-token)
  - Then, with your telegram account create a public channel and invite your bot to it giving it admin status
* Making sure you have Python 3.7+ installed and make sure [PIP](https://docs.python.org/3/installing/index.html) is also installed (check PRAW and python-telegram-bot's requirements)

## Setup Instructions
* Step 1: Install PRAW and python-telegram bot using the Terminal in Linux/Mac or Powershell in Windows

 ```
 py -m pip install praw
 py -m pip install python-telegram-bot
 ```
 
* Step 2: Download all files from this page, keep it in a new folder

* Step 3: Open praw_instance.py in your text editor of choice, and starting on Line 27 fill in the information you obtained from the Reddit API. You can then save and close that file.
  * NOTE: In this code I do not include the "password" and "username" fields as those are only needed from PRAW if you are posting to Reddit. We are only pulling down some information.
  
* Step 4: Open telegram_bot.py and on Line 11 copy and paste in your telegram bot token. Then on Lines 15 and 17 fill in the chat id from your public telegram channel. For example https://t.me/testchannel turns into ``R2T_bot.send_message(chat_id="@testchannel",text=f"{message}")``. 
You can then save and close that file.

* Step 5: From here you have two options, you can use the template provided to create and customize your own method OR you can use the extremely rudimentary Tkinter GUI provided in R2T_gui.py. 

  - Template Option:
