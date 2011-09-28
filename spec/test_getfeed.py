import unittest
import feedparser
from ludibrio import Stub
from should_dsl import should
from getfeed import GetFeed


class TestGetFeed(unittest.TestCase):

    def it_gets_a_feed_from_a_url(self):
        rss = feedparser.FeedParserDict()
        feed = feedparser.FeedParserDict()
        feed.title = "Feed title"
        rss.entries = [feed]
        with Stub() as parse:
            from feedparser import parse
            parse("url") >> rss
        getfeed = GetFeed("url")
        feed = getfeed.get_new_feed()
        feed.title |should| equal_to("Feed title")
