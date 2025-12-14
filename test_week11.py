from app_final.database import get_db
from app_final.services import AuthManager
from app_final.models import SecurityIncident


def test_auth():
    db = get_db()
    auth = AuthManager(db)

    print("\n[TEST] Registering test user 'week11_user'")
    success, msg = auth.register_user("week11_user", "TestPass123!", "user")
    print("  ->", msg)

    print("\n[TEST] Logging in as 'week11_user'")
    user = auth.login_user("week11_user", "TestPass123!")
    if user:
        print("  -> Login successful:", user)
    else:
        print("  -> Login failed")

    db.close()


def test_incidents_list():
    db = get_db()

    print("\n[TEST] Loading some incidents from cyber_incidents table")
    rows = db.fetch_all(
        "SELECT id, incident_type, severity, status, description FROM cyber_incidents LIMIT 5"
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

    for inc in incidents:
        print("  ->", inc)

    db.close()


if __name__ == "__main__":
    test_auth()
    test_incidents_list()