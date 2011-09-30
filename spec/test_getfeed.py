import unittest
import feedparser
from ludibrio import Stub
from should_dsl import should
from getfeed import GetFeed


class TestGetFeed(unittest.TestCase):

    def it_gets_a_feed_from_a_url(self):
        rss = feedparser.FeedParserDict()
        feed = feedparser.FeedParserDict()
        feed.id = 'anything'
        feed.title = "Feed title"
        rss.entries = [feed]
        with Stub() as parse:
            from feedparser import parse
            parse("url") >> rss
        getfeed = GetFeed("url")
        feeds = getfeed.get_new_feed()
        feeds.title |should| equal_to("Feed title")

    def it_retrieves_last_unread_feeds(self):
        with Stub() as feed1: feed1.id >> 1; feed1.title >> '1'
        with Stub() as feed2: feed2.id >> 2; feed2.title >> '2'
        with Stub() as feed3: feed3.id >> 3; feed3.title >> '3'

        with Stub() as parse:
            from feedparser import parse

            rss = feedparser.FeedParserDict()
            rss.entries = [feed1]
            parse("url") >> rss

            rss = feedparser.FeedParserDict()
            rss.entries = [feed2, feed1]
            parse("url") >> rss

            rss = feedparser.FeedParserDict()
            rss.entries = [feed3, feed2, feed1]
            parse("url") >> rss

            rss = feedparser.FeedParserDict()
            rss.entries = [feed3, feed2, feed1]
            parse("url") >> rss

        getfeed = GetFeed('url')

        received_feeds = getfeed.get_new_feed()
        received_feeds.title |should| equal_to('1')

        received_feeds = getfeed.get_new_feed()
        received_feeds.title |should| equal_to("2")

        received_feeds = getfeed.get_new_feed()
        received_feeds.title |should| equal_to("3")

        received_feeds = getfeed.get_new_feed()
        received_feeds |should| be(None)

