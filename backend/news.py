import feedparser

feed = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")

for article in feed.entries[:5]:
    print(article.title)