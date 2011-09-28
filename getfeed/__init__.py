import re
import feedparser
import pynotify


class Feed(object):

    def __init__(self, title):
        self.title = title
        self.alert = pynotify.Notification(title)

    def show(self):
        self.alert.show()


class GetFeed(object):

    def __init__(self, url):
        self.url = url

    def get_last_feed(self):
        rss = feedparser.parse(self.url)
        title = rss.entries[0].title
        feed = Feed(title)
        return feed


def main():
    getfeed = GetFeed("http://planetansi.heroku.com/feeds/githubs")
    feed = getfeed.get_last_feed()
    feed.show()

