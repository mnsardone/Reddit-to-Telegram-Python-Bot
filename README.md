# Reddit-to-Telegram-Python-Bot
Simple bot using [PRAW](https://github.com/praw-dev/praw) and [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (those modules do all the hard stuff). Minimal knowledge of python needed or just follow README.

## Background
Greetings! A few months ago I wrote some very basic code that allowed me to send my GF batches of cute pictures from Reddit. Everyone I told about this was interested so I thought I might as well put the code out their so I can save at least one person a few hours of reading the PRAW documentation and writing this.

## What does it do?
It essentially just aggregates an adjustable number of current top links from a selected subreddit and sends them to a selected telegram chat.

## Setup
Before working with the provided code first you need to have three things ready.
* Obtaining a [Reddit API key](https://www.reddit.com/wiki/api)
* Creating a [Telegram Bot](https://core.telegram.org/bots) and generating its [token](https://core.telegram.org/bots#generating-an-authorization-token)
  - Then, with your telegram account create a public channel and invite your bot to it giving it admin status
* Making sure you have Python 3.7+ installed and make sure [PIP](https://docs.python.org/3/installing/index.html) is also installed (check PRAW and python-telegram-bot's requirements)

## Instructions
