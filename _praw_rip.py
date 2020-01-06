# this is the reddit rip module
import praw


class PullCategory(praw.Reddit):
    """
    This class is a blueprint for various instances of 
    sending specific things to Telegram. Child to praw.Reddit class
    """

    def __init__(self, subredt="all", num_urls=4):
        self.subredt = subredt
        if not isinstance(self.subredt, str):
            raise TypeError("subredt must be a string")
        self.num_urls = num_urls
        if not isinstance(self.num_urls, int):
            raise TypeError("num_urls must be an int")

    def __repr__(self):
        return(f"This is an instance of PullCategory, scrapping from r/{self.subredt}, providing {self.num_urls} URLs")

    def create_outgoing_urls(self):

        outgoing_urls = []

        # this is a read only reddit instance
        reddit = praw.Reddit(client_id="CLIENT ID HERE",
                             client_secret="CLIENT SECRET ID HERE",
                             user_agent="DESCRIPTION HERE")

        # print(reddit.read_only)

        for submission in reddit.subreddit(self.subredt).hot(limit=self.num_urls):
            if not submission.stickied:
                outgoing_urls.append(submission.url)
            else:
                None

        return outgoing_urls
        # print(outgoing_urls)


# TESTING CODE PAST HERE#
# r_aww = PullCategory("aww", 5)
# print(r_aww)
# print(r_aww.create_outgoing_urls())
# note to self, create an instance of pullcategory within CuteBot
