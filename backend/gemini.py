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
        # Parse name and interests from prompt for personalized fallback
        name = "User"
        interests = "your interests"
        for line in prompt.split('\n'):
            if "The user's name is:" in line:
                name = line.split("The user's name is:")[1].strip()
            elif "The user likes:" in line:
                interests = line.split("The user likes:")[1].strip()

        return f"""# Curio Personal News Report for {name}

## Tailored for: {interests}

## Technology Update
New **quantum computing** breakthrough has been achieved.

- This allows qubits to remain *coherent* for much longer than before.
- Quantum supremacy is closer than ever.

## Global Markets
Markets closed at an all-time high today, led by strong gains in **renewable energy** sectors.

- Investors are highly optimistic.
"""
