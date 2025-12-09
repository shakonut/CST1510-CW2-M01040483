import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"Loaded GEMINI_API_KEY? {'YES' if api_key else 'NO'}")
if api_key:
    print("Key prefix:", api_key[:8], "********")

# 2. Configure client
genai.configure(api_key=api_key)

# 3. Simple test call
try:
    model = genai.GenerativeModel("gemini-1.5-flash")  # <- keep this
    response = model.generate_content("Say a short greeting in one sentence.")
    print("\n--- GEMINI RESPONSE ---")
    print(response.text)
except Exception as e:
    print("\n--- GEMINI ERROR ---")
    print(type(e))
    print(e)
    print("----------------------")
