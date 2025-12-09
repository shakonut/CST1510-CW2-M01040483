import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # loads GEMINI_API_KEY from .env

api_key = os.getenv("GEMINI_API_KEY")
print("Loaded GEMINI_API_KEY?", "YES" if api_key else "NO")

genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Say hi in one short sentence.")
    print("\n--- MODEL RESPONSE ---")
    print(response.text)
    print("----------------------")
except Exception as e:
    print("\n--- GEMINI ERROR ---")
    print(type(e), ":", e)
    print("----------------------")