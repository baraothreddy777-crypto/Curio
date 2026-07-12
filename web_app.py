import os
from flask import Flask, render_template, session, request
from backend.app import ask_gemini, news  # Import the news string directly from app.py
from backend.user_agent import name as default_name, topics as default_topics, preferences as default_preferences

app = Flask(__name__)
# Secure secret key for Flask session
app.secret_key = os.getenv("FLASK_SECRET_KEY", "curio-secure-session-key-12345")

@app.route('/')
def home():
    # Allow query parameters to override and save user name/interests in session
    if 'name' in request.args:
        session['name'] = request.args.get('name')
    elif 'name' not in session:
        session['name'] = default_name

    if 'interests' in request.args:
        session['interests'] = request.args.get('interests')
    elif 'interests' not in session:
        session['interests'] = default_topics

    if 'preferences' in request.args:
        session['preferences'] = request.args.get('preferences')
    elif 'preferences' not in session:
        session['preferences'] = default_preferences

    user_name = session['name']
    user_interests = session['interests']
    user_preferences = session['preferences']

    # Create a personalized prompt using the session data
    prompt = f"""
    You are an expert news analyst.
    The user's name is: {user_name}
    The user likes: {user_interests}
    Specific preferences: {user_preferences}

    Write a detailed, comprehensive, and engaging news report personalized for {user_name} based on this news data:
    {news}
    """

    # 2. Get the report from Gemini
    news_report = ask_gemini(prompt)

    # 3. Send to index.html
    return render_template('index.html', news=news_report)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
