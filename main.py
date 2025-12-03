# main.py

from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.user_service import (
    register_user,
    login_user,
    migrate_from_users_txt,
)
from app.data.incidents import (
    load_incidents_from_csv,
    get_all_incidents,
)
from app.data.datasets import load_datasets_from_csv
from app.data.tickets import load_tickets_from_csv


def run_week8_demo():
    print("=" * 60)
    print("Week 8: Database & CRUD Demo")
    print("=" * 60)

    # Connect & create tables
    conn = connect_database()
    create_all_tables(conn)
    conn.close()
    print(" Tables are ready.")

    # Migrate users from Week 7 file
    migrated = migrate_from_users_txt()
    print(f" Migrated {migrated} user(s) from users.txt")

    # Load CSV data for all three domains
    load_incidents_from_csv()
    load_datasets_from_csv()
    load_tickets_from_csv()

    # Quick auth test
    success, msg = register_user("week8_test", "TestPass123!")
    print("Register:", msg)

    success, msg = login_user("week8_test", "TestPass123!")
    print("Login:", msg)

    # Show a sample of incidents
    df = get_all_incidents()
    print("\nSample incidents:")
    print(df.head())


if __name__ == "__main__":
    run_week8_demo()