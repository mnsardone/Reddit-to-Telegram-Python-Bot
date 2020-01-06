import praw_instance
import telegram_bot

# insert name of subreddit in string without the r/
subreddit_name = ""
# insert the amount of posts you would like sent to the channel
amount = 5;
# insert any message you would like the preface the posts with in the string
message = ""

my_method = praw_instance.PullCategory(subreddit_name, amount)

telegram_bot.send_R2T_bot(my_method, message)
