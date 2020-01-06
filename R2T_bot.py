# This is the R2PBot Module
import telegram
import _praw_rip


def send_R2T_bot(pull_cat, message):
    if not isinstance(pull_cat, _praw_rip.PullCategory):
        raise TypeError("This needs to be an instance off PullCategory")
    else:
        R2T_bot = telegram.Bot(
            token="PLACE TOKEN HERE")
        print(R2T_bot.get_me())

        R2T_bot.send_message(chat_id="@BLANK",
                             text=f"{message}")
        for url in pull_cat.create_outgoing_urls():
            R2T_bot.send_message(chat_id="@BLANK", text=f"{url}")
