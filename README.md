# CST1510 Coursework 2 – Multi-Domain Intelligence Platform

Student: Shakeeb (M01040483)  
Module: CST1510 – Introduction to Programming (Python)  
Lecturer: Santhosh Menon

This coursework is a step-by-step project where I build a small “Multi-Domain Intelligence Platform” in Python.  
The idea is to move from a simple login script to a proper dashboard with data, security and basic AI features.

---

## Project Goals

- Learn Python functions, file handling and data structures.
- Build a secure login system using hashed passwords.
- Store and manage data in text files, CSV and SQLite.
- Create simple dashboards using Streamlit.
- Use APIs (OpenAI) and basic session state to make the app feel more real.
- Keep everything version-controlled in Git and pushed to GitHub.

---

## Week 7 – Secure Authentication System

**Focus:** Password hashing and file-based user storage. :contentReference[oaicite:0]{index=0}  

### What I built
- `auth.py` – main program with **Register** and **Login** menu.
- Uses **bcrypt** to hash passwords before saving them.
- Stores user data in `users.txt` as: `username,hashed_password`.
- Uses `with open(...)` and simple functions to keep code tidy.

### Main features
- Register new user (checks for duplicates).
- Login with username + password.
- Uses a virtual environment (`.venv`) with `bcrypt` installed.
- Basic input validation and friendly error messages.

### Key files
- `auth.py`
- `users.txt`
- `.gitignore`
- `requirements.txt`
- `README.md`

---

## Week 8 – SQLite Database & CSV Import

**Focus:** Moving from text files to a small SQLite database.

### What I built
- `week8_database.py` (or later `app/data/db.py` style) with helper functions:
  - Create a database connection.
  - Create tables if they do not exist.
  - Import data from CSV into tables.
- Used the three CSV files from the `DATA/` folder:
  - `cyber_incidents.csv`
  - `datasets_metadata.csv`
  - `it_tickets.csv`
- Loaded the incidents CSV into a table and checked the row count.

### Main features
- Uses `sqlite3` to create `multi_domain.db`.
- Reads CSV safely with `csv.reader` and `newline=""`.
- Automatically builds table columns from the CSV header row.
- Inserts all rows and prints how many were loaded (e.g. “Imported 115 rows”).

### Key files (Week 8)
- `week8_database.py`  (database + CSV import logic)
- `multi_domain.db`    (generated SQLite database file)
- `DATA/cyber_incidents.csv`
- `DATA/datasets_metadata.csv`
- `DATA/it_tickets.csv`

---

## Week 9 – Streamlit Mini Dashboards

**Focus:** First Streamlit front-end and simple interactive widgets.

### What I built
From the lab and workshop templates I set up several Streamlit scripts:

- `basic_page_elements.py` – titles, headers, markdown text.
- `basic_interactive_widgets.py` – buttons, sliders, text input, select boxes.
- `layout_demo.py` – columns and sidebars to control layout.
- `mini_dashboard.py` – combines elements into a small dashboard page
  (e.g. filters, summary text, and simple charts or counts).

All of these are meant to be run with:

```bash
streamlit run mini_dashboard.py