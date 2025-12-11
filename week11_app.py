import sys
from pathlib import Path

# Make sure the project root is on sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

import streamlit as st

from database.db import get_db
from services.auth_manager import AuthManager
from services.database_manager import DatabaseManager
from models.security_incident import SecurityIncident


# Helper functions
def get_auth_manager() -> AuthManager:
    db: DatabaseManager = get_db()
    return AuthManager(db)


def fetch_incidents(limit: int = 10) -> list[SecurityIncident]:
    db: DatabaseManager = get_db()

    rows = db.fetch_all(
        """
        SELECT id, incident_type, severity, status, description
        FROM cyber_incidents
        ORDER BY id
        LIMIT ?
        """,
        (limit,),
    )

    incidents: list[SecurityIncident] = []
    for row in rows:
        incident = SecurityIncident(
            incident_id=row[0],
            incident_type=row[1],
            severity=row[2],
            status=row[3],
            description=row[4],
        )
        incidents.append(incident)

    db.close()
    return incidents


# Streamlit page setup

st.set_page_config(
    page_title="Week 11 – OOP Refactor Demo",
    page_icon="🧩",
    layout="wide",
)

st.title("Week 11 – OOP Refactor Demo")
st.write(
    "This app shows a simple login using AuthManager and a cybersecurity view "
    "that uses SecurityIncident objects loaded from the SQLite database."
)

# Session state for logged in user

if "user" not in st.session_state:
    st.session_state.user = None  # will hold a User object from models.user



# Sidebar navigation

menu = st.sidebar.radio("Navigation", ["Login", "Cybersecurity"])


# Login Page

if menu == "Login":
    st.subheader("🔐 Login")

    col1, col2 = st.columns(2)

    with col1:
        username = st.text_input("Username")

    with col2:
        password = st.text_input("Password", type="password")

    login_button = st.button("Log in")
    register_button = st.button("Quick register (demo user)")

    auth = get_auth_manager()

    if login_button:
        user = auth.login_user(username.strip(), password)
        if user:
            st.session_state.user = user
            st.success(f"Logged in as **{user.get_username()}** (role: {user.get_role()})")
        else:
            st.error("Login failed. Please check your username or password.")

    if register_button:
        if not username or not password:
            st.warning("Please enter a username and password before registering.")
        else:
            ok, msg = auth.register_user(username.strip(), password)
            if ok:
                st.success(msg)
            else:
                st.error(msg)

    # current login status
    st.divider()
    if st.session_state.user:
        st.info(f"Current user: {st.session_state.user}")
        if st.button("Log out"):
            st.session_state.user = None
            st.warning("You have been logged out.")
    else:
        st.info("No user is currently logged in.")

# Cybersecurity Page

elif menu == "Cybersecurity":
    st.subheader("🛡️ Cybersecurity – Recent Incidents")

    if not st.session_state.user:
        st.warning("You must log in on the 'Login' page before viewing incidents.")
    else:
        st.success(f"Logged in as {st.session_state.user.get_username()}")

        st.write(
            "Below is a small sample of incidents loaded from the "
            "`cyber_incidents` table in the SQLite database and wrapped "
            "in SecurityIncident model objects."
        )

        limit = st.slider("Number of incidents to show", min_value=5, max_value=50, value=10, step=5)

        incidents = fetch_incidents(limit=limit)

        # simple table for display
        table_data = []
        for inc in incidents:
            table_data.append(
                {
                    "ID": inc.get_id(),
                    "Type": inc.get_type(),
                    "Severity": inc.get_severity(),
                    "Status": inc.get_status(),
                    "High severity?": "Yes" if inc.is_high_severity() else "No",
                    "Description": inc.get_description(),
                }
            )

        st.table(table_data)