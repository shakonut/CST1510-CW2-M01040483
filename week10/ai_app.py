import streamlit as st
from ai_helper import ask_gemini   # because ai_helper.py is in the same folder

st.set_page_config(page_title="Week 10 – AI Assistant Demo")

st.title("Week 10 – AI Assistant Demo (Gemini / Fallback)")

st.write(
    "This page sends a question to Gemini using our helper function. "
    "If the API call fails, we show the error message instead of "
    "crashing the app."
)

user_input = st.text_area("Ask a question:", height=120)

if st.button("Send"):
    question = user_input.strip()

    if not question:
        st.warning("Please type a question first.")
    else:
        with st.spinner("Thinking..."):
            answer = ask_gemini(question)

        st.subheader("Response")
        st.write(answer)