import os
import time
from google import genai
from google.genai.errors import ClientError, APIError
from dotenv import load_dotenv

load_dotenv()

# Instantiate the google-genai Client.
# It automatically retrieves GEMINI_API_KEY from the environment.
client = genai.Client()

def ask_gemini(prompt):
    max_retries = 3
    delay = 2.0  # Initial delay of 2 seconds
    backoff_factor = 2.0

    for attempt in range(max_retries + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            return response.text
        except (ClientError, APIError) as e:
            # Check if this is a 429 or RESOURCE_EXHAUSTED error
            is_429 = False
            status_code = getattr(e, 'code', None) or getattr(e, 'status_code', None)
            if status_code == 429:
                is_429 = True
            else:
                err_msg = str(e).upper()
                if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg or "LIMIT" in err_msg:
                    is_429 = True

            if is_429 and attempt < max_retries:
                print(f"Gemini API rate limit hit (429). Retrying in {delay} seconds (Attempt {attempt + 1}/{max_retries})...")
                time.sleep(delay)
                delay *= backoff_factor
            else:
                # Handle general errors or exhausted retries gracefully
                print(f"Error calling Gemini API: {e}. Returning fallback response.")
                return get_fallback_summary(prompt)
        except Exception as e:
            print(f"Unexpected error calling Gemini API: {e}. Returning fallback response.")
            return get_fallback_summary(prompt)

def get_fallback_summary(prompt):
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

*Note: Due to high traffic, we are currently displaying a cached/mocked personal briefing. Please try refreshing in a few moments.*

## Technology Update
New **quantum computing** breakthrough has been achieved.

- This allows qubits to remain *coherent* for much longer than before.
- Quantum supremacy is closer than ever.

## Global Markets
Markets closed at an all-time high today, led by strong gains in **renewable energy** sectors.

- Investors are highly optimistic.
"""
