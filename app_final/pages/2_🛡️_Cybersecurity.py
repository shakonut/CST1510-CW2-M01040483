# pages/2_🛡️_Cybersecurity.py

# Ensure project root is importable when running Streamlit pages/
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
import sqlite3

from app_final.models.security_incident import SecurityIncident


DB_PATH = ROOT_DIR / "DATA" / "intelligence_platform.db"


def require_login() -> bool:
    """Block page if user is not logged in."""
    if "user" not in st.session_state or st.session_state.user is None:
        st.warning("You must log in first. Open the Login page in the sidebar.")
        return False
    return True


def get_existing_columns(conn: sqlite3.Connection, table_name: str) -> list[str]:
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table_name});")
    return [row[1] for row in cur.fetchall()]  # row[1] = column name


def pick_column(cols: list[str], options: list[str]) -> str | None:
    """Pick the first matching column name from a list of possible options."""
    lower_map = {c.lower(): c for c in cols}
    for opt in options:
        if opt.lower() in lower_map:
            return lower_map[opt.lower()]
    return None


def load_incidents(limit: int = 50) -> list[SecurityIncident]:
    """
    Load incidents from cyber_incidents table.
    This function is defensive: it tries to match common column names.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        table = "cyber_incidents"
        cols = get_existing_columns(conn, table)

        if not cols:
            return []

        # Try to match likely column names (based on common CSVs)
        col_id = pick_column(cols, ["id", "incident_id", "Incident_Number", "incident_number"])
        col_type = pick_column(cols, ["incident_type", "type", "Category", "category", "Incident_Type"])
        col_sev = pick_column(cols, ["severity", "Severity", "priority", "Priority"])
        col_status = pick_column(cols, ["status", "Status", "state", "State"])
        col_desc = pick_column(cols, ["description", "Description", "details", "Details", "summary", "Summary"])

        # If some are missing, we still proceed by selecting any columns available
        select_cols = [c for c in [col_id, col_type, col_sev, col_status, col_desc] if c is not None]
        if not select_cols:
            select_cols = cols[:5]  # fallback

        query = f"SELECT {', '.join(select_cols)} FROM {table} LIMIT ?"
        rows = conn.execute(query, (limit,)).fetchall()

        incidents: list[SecurityIncident] = []
        for r in rows:
            # Defensive fetch with fallbacks
            incident_id = str(r[col_id]) if col_id else "N/A"
            incident_type = str(r[col_type]) if col_type else "Unknown"
            severity = str(r[col_sev]) if col_sev else "Unknown"
            status = str(r[col_status]) if col_status else "Unknown"
            description = str(r[col_desc]) if col_desc else ""

            incidents.append(
                SecurityIncident(
                    incident_id=incident_id,
                    incident_type=incident_type,
                    severity=severity,
                    status=status,
                    description=description,
                )
            )
        return incidents
    finally:
        conn.close()


def severity_counts() -> dict[str, int]:
    conn = sqlite3.connect(DB_PATH)
    try:
        cols = get_existing_columns(conn, "cyber_incidents")
        col_sev = pick_column(cols, ["severity", "Severity", "priority", "Priority"])
        if not col_sev:
            return {}

        cur = conn.cursor()
        cur.execute(
            f"SELECT {col_sev}, COUNT(*) FROM cyber_incidents GROUP BY {col_sev} ORDER BY COUNT(*) DESC;"
        )
        results = cur.fetchall()
        return {str(sev): int(cnt) for sev, cnt in results}
    finally:
        conn.close()


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🛡️ Cybersecurity Dashboard")

if not require_login():
    st.stop()

st.success(f"Logged in as: {st.session_state.user.get_username()}")

limit = st.slider("How many incidents to show", 10, 200, 50, step=10)
incidents = load_incidents(limit=limit)

st.subheader("Recent incidents")
if not incidents:
    st.error(
        "No incident data found. Make sure your Week 8 CSV data was loaded into the database "
        "and the table `cyber_incidents` exists."
    )
else:
    # Show as table
    table_rows = []
    for inc in incidents:
        table_rows.append(
            {
                "Incident ID": inc.get_id(),
                "Type": inc.get_type(),
                "Severity": inc.get_severity(),
                "Status": inc.get_status(),
                "High severity?": "Yes" if inc.is_high_severity() else "No",
                "Description": inc.get_description(),
            }
        )
    st.table(table_rows)

st.divider()

st.subheader("Incidents by severity")
sev = severity_counts()
if not sev:
    st.info("Severity column not found in your table, so I can't build this chart yet.")
else:
    st.bar_chart(sev)

st.divider()

st.subheader("Quick insight (write this in your report)")
if sev:
    top = list(sev.items())[0]
    st.write(
        f"- The most common severity level is **{top[0]}** with **{top[1]}** incidents.\n"
        f"- This helps identify where response effort should be focused."
    )
else:
    st.write("- Once severity is available, this section will highlight the biggest incident category/severity.")