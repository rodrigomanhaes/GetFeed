import re
import feedparser
import pynotify
from apscheduler.scheduler import Scheduler


class Feed(object):

    def __init__(self, title):
        self.title = title
        self.alert = pynotify.Notification(title)

    def show(self):
        self.alert.show()


class GetFeed(object):

    def __init__(self, url):
        self.url = url

    def get_new_feed(self):
        rss = feedparser.parse(self.url)
        title = rss.entries[0].title
        feed = Feed(title)
        return feed


def main():
    sched = Scheduler()
    @sched.interval_schedule(seconds=10)
    def show_last_feed():
        getfeed = GetFeed("http://planetansi.heroku.com/feeds/githubs")
        feed = getfeed.get_new_feed()
        if feed:
            feed.show()
    sched.start()
    while sched.running:
        pass

