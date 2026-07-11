import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Instantiate the google-genai Client.
# It automatically retrieves GEMINI_API_KEY from the environment.
client = genai.Client()

def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text
