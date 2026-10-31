

The GitHub Actions build is failing because:

1. The old model gemini-1.5-flash is not found.
2. The old google.generativeai Python package is deprecated.

Make these changes:

1. Replace the old package with the official google-genai SDK.
2. Update all imports to:
   from google import genai

3. Initialize the Gemini client using:
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

4. Replace the old model with:
   gemini-3.8-flash

5. Update content generation to use:
   response = client.models.generate_content(
       model="gemini-3.8-flash",
       contents=prompt
   )

6. Update requirements.txt.
7. Check all Python files for old Gemini imports and model names.
8. Keep my existing YouTube automation workflow intact.
9. Do not remove YouTube upload, video generation,
   title, description, tags or scheduling features.
10. Check for other errors.
11. Commit and push all fixes.
12. Run GitHub Actions again and verify the build.

Do not expose or delete my API keys.
