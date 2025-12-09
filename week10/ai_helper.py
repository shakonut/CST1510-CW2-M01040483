import os
from dotenv import load_dotenv

try:
    import google.generativeai as genai
    HAS_GEMINI = True
except Exception:
    genai = None
    HAS_GEMINI = False


def ask_gemini(prompt: str) -> str:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        # No key set
        return (
            "AI is not available right now because GEMINI_API_KEY "
            "is missing in the .env file.\n\n"
            f"You asked: {prompt}"
        )

    if not HAS_GEMINI:
        # Library not imported
        return (
            "AI library (google-generativeai) is not available in this "
            "environment.\n\n"
            f"You asked: {prompt}"
        )

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # No crash, just explanation.
        return (
            "AI call failed (likely due to old library / model not found).\n"
            f"Error type: {e.__class__.__name__}\n"
            f"Message: {e}\n\n"
            "For coursework purposes this shows that the AI integration\n"
            "was attempted, but the external API could not be used.\n\n"
            f"You asked: {prompt}"
        )