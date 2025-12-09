import streamlit as st

# -----------------------------
# Week 10 – Initial Setup
# -----------------------------
st.title("Week 10 – ChatGPT Style Chat Application")

# Create session_state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your Week 10 assistant."}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------------
# Fake AI Model (Gemini fallback)
# -----------------------------
def fake_ai_response(user_text):
    # Simulated response because Gemini API isn't available
    return f"I received your message: '{user_text}'. (Simulated AI Response)"

# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input("Type a message...")

if user_input:
    # Add user message to session_state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display immediately
    with st.chat_message("user"):
        st.write(user_input)

    # Generate assistant response
    ai_reply = fake_ai_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    with st.chat_message("assistant"):
        st.write(ai_reply)