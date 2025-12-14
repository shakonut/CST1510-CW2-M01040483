# pages/1_🔐_Login.py

# Ensure project root is importable when running Streamlit pages/
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

# Reuse your Week 11 OOP/service layer
from app_final.services.database_manager import DatabaseManager
from app_final.services.auth_manager import AuthManager


DB_PATH = ROOT_DIR / "DATA" / "intelligence_platform.db"


def ensure_users_table(db: DatabaseManager) -> None:
    """
    Week 7/8/11 bridge: make sure the users table exists.
    This prevents "no such table: users" when you run login first time.
    """
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        );
        """,
        commit=True,
    )


def get_auth() -> tuple[DatabaseManager, AuthManager]:
    """
    Create DB manager + Auth manager for this request.
    Streamlit reruns scripts often, so we keep it simple and make new ones.
    """
    db = DatabaseManager(DB_PATH)
    db.connect()
    ensure_users_table(db)
    auth = AuthManager(db)
    return db, auth


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🔐 Login (Week 11 OOP)")

# Session state
if "user" not in st.session_state:
    st.session_state.user = None  # will store a User object


tab_login, tab_register = st.tabs(["Login", "Register"])

with tab_login:
    st.subheader("Login")

    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Log in"):
        db, auth = get_auth()
        try:
            user = auth.login_user(username.strip(), password)
            if user:
                st.session_state.user = user
                st.success(f"Logged in as **{user.get_username()}** (role: {user.get_role()})")
            else:
                st.error("Login failed. Wrong username or password.")
        finally:
            db.close()

    st.divider()
    if st.session_state.user:
        st.info(f"Current session user: {st.session_state.user}")
        if st.button("Log out"):
            st.session_state.user = None
            st.warning("Logged out.")

with tab_register:
    st.subheader("Register")

    new_username = st.text_input("New username", key="reg_user")
    new_password = st.text_input("New password", type="password", key="reg_pass")
    confirm_password = st.text_input("Confirm password", type="password", key="reg_pass2")

    role = st.selectbox("Role (keep as user unless told otherwise)", ["user", "admin"], index=0)

    if st.button("Create account"):
        if not new_username.strip():
            st.warning("Please enter a username.")
        elif not new_password:
            st.warning("Please enter a password.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            db, auth = get_auth()
            try:
                ok, msg = auth.register_user(new_username.strip(), new_password, role=role)
                if ok:
                    st.success(msg)
                    st.info("Now go to the Login tab and log in.")
                else:
                    st.error(msg)
            finally:
                db.close()