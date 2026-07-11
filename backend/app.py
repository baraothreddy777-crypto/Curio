from backend.user_agent import *
from backend.gemini import ask_gemini
import feedparser  # You MUST have this line here

feed = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")

news = ""

# Option 1: Search more articles (50) and check both title AND summary
for article in feed.entries[:50]:
    if topics.lower() in article.title.lower() or topics.lower() in article.summary.lower():
        news += "- " + article.title + ": " + article.summary + "\n"

# Fallback if no specific matches found
if news == "":
    for article in feed.entries[:10]:
        news += "- " + article.title + "\n"

# Option 2: The much more detailed prompt
prompt = f"""
You are an expert news analyst.
The user likes: {topics}
Specific preferences: {preferences}

Write a detailed, comprehensive, and engaging news report based on the provided headlines.
1. Provide deep context and explain why these stories matter.
2. Focus heavily on {topics} and {preferences}.
3. Use a professional but engaging tone.
4. If there are not enough articles on the requested topics, summarize the most important global news with high detail.

Here is the news data to summarize:
{news}
"""

print("\n" + "="*50)
print("YOUR PERSONALIZED NEWS BRIEF")
print("="*50 + "\n")

print(ask_gemini(prompt))

print("\n" + "="*50)
