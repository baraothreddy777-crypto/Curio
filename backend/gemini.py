import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Instantiate the google-genai Client.
# It automatically retrieves GEMINI_API_KEY from the environment.
client = genai.Client()

def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        print(f"Error calling Gemini: {e}. Falling back to mock summary.")
        return """# Curio Personal News Report

## Technology Update
New **quantum computing** breakthrough has been achieved.

- This allows qubits to remain *coherent* for much longer than before.
- Quantum supremacy is closer than ever.

## Global Markets
Markets closed at an all-time high today, led by strong gains in **renewable energy** sectors.

- Investors are highly optimistic.
"""
