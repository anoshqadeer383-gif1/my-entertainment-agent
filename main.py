import os
import google.generativeai as genai

# Get API key from GitHub Secrets
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: API key nahi mili!")
    exit(1)

# Connect to Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-3.8.flash')

print("Gemini se connect ho gaya! Script likh raha hai...")

# Generate a test script
response = model.generate_content("Write a very short, funny 2-sentence script for a YouTube Short about a lazy cat.")

print("--- YEH HAMARA TEST SCRIPT HAI ---")
print(response.text)
print("----------------------------------")
