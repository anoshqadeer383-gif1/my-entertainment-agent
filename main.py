import os
from google import genai

# 1. Keep API keys in environment secrets
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in environment secrets.")
    exit(1)

# 2. Initialize the new google-genai SDK
client = genai.Client(api_key=api_key)

print("Gemini se connect ho gaya! Script likh raha hai...")

# 3. Use the supported model gemini-flash-latest
prompt = "Write a very short, funny 2-sentence script for a YouTube Short about a lazy cat."

try:
    response = client.models.generate_content(
        model='gemini-flash-latest',
        contents=prompt
    )
    
    print("--- YEH HAMARA TEST SCRIPT HAI ---")
    print(response.text)
    print("----------------------------------")
    
    # ==========================================
    # FUTURE YOUTUBE AUTOMATION FEATURES (Preserved)
    # ==========================================
    # TODO: 4. Video Generation (MoviePy/FFmpeg)
    # TODO: 5. YouTube Upload (YouTube Data API v3)
    
    print("Video generation aur YouTube upload ka setup agle step mein hoga.")

except Exception as e:
    print(f"Error aaya: {e}")
