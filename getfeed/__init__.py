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
        self.last_received_id = None

    def get_new_feed(self):
        rss = feedparser.parse(self.url)
        titles = []
        if len(rss.entries) > 0 and rss.entries[0].id != self.last_received_id:
            entry = rss.entries[0]
            self.last_received_id = entry.id
            return Feed(entry.title)


def main():
    sched = Scheduler()
    getfeed = GetFeed("http://planetansi.heroku.com/feeds/githubs")
    @sched.interval_schedule(seconds=2)
    def show_last_feed():
        feeds = getfeed.get_new_feed()
        feeds.show()
    sched.start()
    while sched.running:
        pass

