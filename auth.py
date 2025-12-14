"""
Week 7 – Secure Authentication System for CW2
"""

import bcrypt
import os


# File where user data is stored
USER_DATA_FILE = "app_final/users.txt"


def hash_password(plain_text_password: str) -> str:
    """
    Return a bcrypt hash for the given plaintext password as a UTF-8 string.
    """
    # bcrypt needs bytes so encode the string
    password_bytes = plain_text_password.encode("utf-8")
    # generate a random salt
    salt = bcrypt.gensalt()
    # hash the password + salt
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    # store as normal string
    return hashed_bytes.decode("utf-8")


def verify_password(plain_text_password: str, hashed_password: str) -> bool:
    """
    Check a plaintext password against a stored bcrypt hash.
    Returns True if they match, False otherwise.
    """
    password_bytes = plain_text_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)


def user_exists(username: str) -> bool:
    """
    Return True if username is already in users.txt, else False.
    """
    if not os.path.exists(USER_DATA_FILE):
        # File not created yet - no users
        return False

    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            stored_user, _ = line.split(",", 1)
            if stored_user == username:
                return True
    return False


def register_user(username: str, password: str) -> bool:
    """
    Register a new user (username, bcrypt-hash(password)).
    Returns True if success; False if username already exists.
    """
    if user_exists(username):
        print(f"Error: username '{username}' already exists.")
        return False

    hashed = hash_password(password)
    with open(USER_DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{hashed}\n")

    print(f"User '{username}' registered.")
    return True


def login_user(username: str, password: str) -> bool:
    """
    Return True if username+password are valid, else False.
    """
    if not os.path.exists(USER_DATA_FILE):
        print("No users registered yet.")
        return False

    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            stored_user, stored_hash = line.split(",", 1)
            if stored_user == username:
                # Found the user – verify password
                return verify_password(password, stored_hash)

    # Username not found
    return False


def display_menu() -> None:
    """Display menu options."""
    print("\n" + "=" * 50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System (Week 7)")
    print("=" * 50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-" * 50)


def main() -> None:
    """Main program loop."""
    print("\nWelcome to the Week 7 Authentication System!")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1–3): ").strip()

        if choice == "1":
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            confirm = input("Confirm password: ").strip()

            if password != confirm:
                print("Error: passwords do not match.")
                continue

            register_user(username, password)

        elif choice == "2":
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            if login_user(username, password):
                print("\nLogin successful. You are now logged in.")
            else:
                print("\nLogin failed. Check your username or password.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()