# CST1510 Coursework 2 – Multi-Domain Intelligence Platform

Student: **Shakeeb (M01040483)**
Module: **CST1510 – Introduction to Programming (Python)**
Lecturer: **Santhosh Menon**

---

## Project Overview

This coursework is a step-by-step project where I developed a **Multi-Domain Intelligence Platform** using Python.
The project progresses from basic authentication scripts to a modular, database-driven Streamlit application with cybersecurity and AI-related features.

The aim of this coursework is to demonstrate my understanding of Python fundamentals, databases, modular design, and interactive web applications.

---

## Project Goals

* Learn Python functions, file handling, and data structures
* Build a secure authentication system using hashed passwords
* Store and manage data using text files, CSV files, and SQLite databases
* Create interactive dashboards using Streamlit
* Experiment with API integration and session state
* Apply modular programming principles
* Use Git and GitHub for version control throughout development

---

## Week 7 – Secure Authentication System

**Focus:** Password hashing and file-based user storage

### What I built

* `auth.py` – a menu-based program with **Register** and **Login** functionality
* Passwords are securely hashed using **bcrypt** before storage
* User credentials are stored in `users.txt` in the format:

  ```
  username,hashed_password
  ```
* Used functions and file handling (`with open(...)`) to keep the code clean

### Main features

* User registration with duplicate username checking
* Secure login using password verification
* Virtual environment (`.venv`) for dependency isolation
* Basic input validation and user-friendly messages

### Key files (Week 7)

* `auth.py`
* `users.txt`
* `requirements.txt`
* `.gitignore`

---

## Week 8 – SQLite Database & CSV Import

**Focus:** Moving from text files to a small SQLite database

### What I built

* A database helper script (`week8_database.py` or later `app/data/db.py` style) containing functions to:

  * Create a database connection
  * Create tables if they do not already exist
  * Import data from CSV files into database tables

* Used three CSV datasets stored in the `DATA/` folder:

  * `cyber_incidents.csv`
  * `datasets_metadata.csv`
  * `it_tickets.csv`

* Imported cybersecurity incidents into an SQLite table and verified row counts

### Main features

* Uses `sqlite3` to create a local database (e.g. `multi_domain.db`)
* Reads CSV files safely using `csv.reader` with `newline=""`
* Automatically creates table columns based on CSV header rows
* Inserts all records and confirms successful imports

### Key files (Week 8)

* `week8_database.py`
* `multi_domain.db`
* `DATA/cyber_incidents.csv`
* `DATA/datasets_metadata.csv`
* `DATA/it_tickets.csv`

---

## Week 9 – Streamlit Mini Dashboards

**Focus:** Building simple interactive dashboards using Streamlit

### What I built

I created multiple small Streamlit applications to understand how Python scripts can be transformed into web-based dashboards.

### Main features

* Learned how Streamlit runs Python files as web applications
* Used widgets such as:

  * Buttons
  * Sliders
  * Text inputs
  * Select boxes
* Used `st.session_state` to store values between interactions
* Explored layout features such as columns and sidebars

### Key files (Week 9)

* `basic_page_elements.py`
* `basic_interactive_widgets.py`
* `layout_demo.py`
* `mini_dashboard.py`

---

## Week 10 – AI Integration & Session State

**Focus:** API integration, session state, and error handling

### What I built

* Experimented with AI-style API integration (OpenAI / Gemini style)

* Created Streamlit apps that:

  * Accept user input
  * Send prompts to an AI helper function
  * Display responses in the UI

* Used `st.session_state` to store chat history

* Added `try/except` blocks to handle API failures gracefully

### Main features

* Clear separation between UI code and AI logic
* Safe handling of missing models or API errors
* Demonstrated correct integration approach even when APIs failed
* Followed lab requirements for AI experimentation

### Key files (Week 10)

* `openai_api_streamlit.py`
* `chatGpt_text_base.py`
* `example_using_sessions.py`
* `.env` (used locally, not committed)

---

## Week 11 – Project Refactoring & Modular Design

**Focus:** Code refactoring and modular project structure

### What I built

* Refactored the project into structured folders:

  * `models/` – data models (User, SecurityIncident, Dataset, Ticket)
  * `services/` – business logic (authentication, database access, AI helpers)
  * `database/` – database connection utilities

* Introduced classes to replace long procedural scripts

* Reused database and authentication logic across multiple Streamlit pages

### Main features

* Separation of concerns (UI, logic, data)
* Reusable database connection via `get_db()`
* Cleaner imports and improved readability
* Prepared codebase for Coursework 2

### Key files (Week 11)

* `models/security_incident.py`
* `services/auth_manager.py`
* `services/database_manager.py`
* `database/db.py`
* `week11_app.py`

---

## Coursework 2 – Multi-Domain Intelligence Platform

**Goal:** Combine all weekly work into a single structured application

### Application features

* **Main App (`app.py`)**

  * Landing page describing the platform

* **Login Page**

  * User authentication using stored credentials
  * Session-based login state

* **Cybersecurity Page**

  * Displays cybersecurity incidents from the database
  * Uses `SecurityIncident` model objects

* **Database**

  * SQLite database storing incidents and user-related data

* **Design**

  * Multi-page Streamlit navigation
  * Sidebar-based user experience

### Technologies used

* Python 3.12
* Streamlit
* SQLite
* bcrypt
* pandas
* Git & GitHub

---

## Reflection

This coursework helped me understand how individual Python concepts combine to form a complete application. Throughout the project, I learned how to:

* Structure Python projects properly
* Separate logic from user interfaces
* Handle errors instead of allowing programs to crash
* Use Git for version control consistently
* Work confidently with databases and Streamlit applications

Overall, this project showed me how Python can be used beyond basic scripts to build structured, interactive, and real-world applications.
