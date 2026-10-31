import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: API key nahi mili!")
    exit(1)

print("Gemini se connect ho raha hai...")
client = genai.Client(api_key=api_key)

print("Script likhi ja rahi hai...")
response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents="Write a very short, funny 2-sentence script for a YouTube Short about a lazy cat."
)

print("--- YEH HAMARA TEST SCRIPT HAI ---")
print(response.text)
print("----------------------------------")
