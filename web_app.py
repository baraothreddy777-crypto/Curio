from flask import Flask, render_template
from backend.app import ask_gemini, news  # Import the news string directly from app.py
from backend.user_agent import topics, preferences

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Create the prompt using the news already fetched by app.py
    prompt = f"""
    You are an expert news analyst.
    The user likes: {topics}
    Specific preferences: {preferences}

    Write a detailed, comprehensive, and engaging news report based on this news data:
    {news}
    """

    # 2. Get the report from Gemini
    news_report = ask_gemini(prompt)

    # 3. Send to index.html
    return render_template('index.html', news=news_report)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)