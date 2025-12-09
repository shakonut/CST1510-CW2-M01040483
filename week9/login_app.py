import streamlit as st

# ---------- Page setup ----------
st.set_page_config(
    page_title="Week 9 Login Demo",
    page_icon="🔐",
    layout="centered"
)

st.title("Week 9 – Simple Login App")
st.write("This is my own Streamlit login page built for Week 9.")

# ---------- Demo user data ----------
# In a real app this would come from a database.
# Here it's just a small dictionary for the demo.
USERS = {
    "alice": {"password": "1234", "role": "Data Scientist"},
    "bob": {"password": "5678", "role": "Cyber Analyst"},
    "mag": {"password": "9999", "role": "IT Support"}
}

# ---------- Session state ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None


def check_login(username: str, password: str) -> bool:
    """Return True if the username + password match our demo users."""
    user = USERS.get(username)
    if user is None:
        return False
    return password == user["password"]


# ---------- Layout ----------
st.subheader("Login")

col1, col2 = st.columns(2)

with col1:
    username_input = st.text_input("Username")

with col2:
    password_input = st.text_input("Password", type="password")

remember_me = st.checkbox("Remember me on this session")

login_button = st.button("Log in")

# ---------- Logic ----------
if login_button:
    if check_login(username_input.strip(), password_input):
        st.session_state.logged_in = True
        st.session_state.username = username_input.strip()

        st.success(f"Login successful – welcome {username_input}!")
        if remember_me:
            st.info("✅ You chose 'Remember me' for this session.")
    else:
        st.error("Login failed. Please check your username or password.")

# ---------- Logged-in area ----------
if st.session_state.logged_in:
    st.divider()
    st.subheader("User dashboard")

    user_info = USERS.get(st.session_state.username, {})
    role = user_info.get("role", "User")

    st.write(f"**User:** {st.session_state.username}")
    st.write(f"**Role:** {role}")

    mood = st.slider("How is your mood today (0 = bad, 10 = great)?", 0, 10, 7)
    st.write(f"Thanks! You rated your mood as **{mood}/10**.")

    if st.button("Log out"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.warning("You have been logged out.")