from gemini import ask_gemini
import feedparser

feed = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")

news = ""

for article in feed.entries[:5]:
    news += "- " + article.title + "\n"

prompt = f"""
Summarize these news headlines in simple English:

{news}
"""

result = ask_gemini(prompt)

print(result)