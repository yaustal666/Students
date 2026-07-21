import sqlite3
import hashlib
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "surgery_scheduler.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def init_db():
    conn = get_connection()
    c = conn.cursor()

    # ── Users ──────────────────────────────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            username   TEXT    UNIQUE NOT NULL,
            password   TEXT    NOT NULL,
            role       TEXT    NOT NULL CHECK(role IN ('admin','nurse','surgeon')),
            full_name  TEXT    NOT NULL,
            created_at TEXT    DEFAULT (datetime('now'))
        )
    """)

    # ── Surgeons ───────────────────────────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS surgeons (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT NOT NULL,
            specialty  TEXT NOT NULL,
            phone      TEXT,
            email      TEXT,
            available  INTEGER DEFAULT 1,
            user_id    INTEGER REFERENCES users(id),
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)

    # ── Patients ───────────────────────────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT NOT NULL,
            dob        TEXT,
            gender     TEXT,
            phone      TEXT,
            blood_type TEXT,
            allergies  TEXT,
            notes      TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)

    # ── Equipment ──────────────────────────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS equipment (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            name         TEXT NOT NULL,
            category     TEXT NOT NULL,
            quantity     INTEGER DEFAULT 1,
            available    INTEGER DEFAULT 1,
            sterilized   INTEGER DEFAULT 0,
            last_service TEXT,
            notes        TEXT
        )
    """)

    # ── Operating Rooms ────────────────────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS operating_rooms (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            floor  TEXT,
            status TEXT DEFAULT 'available'
        )
    """)

    # ── Surgeries ──────────────────────────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS surgeries (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id     INTEGER NOT NULL REFERENCES patients(id),
            surgeon_id     INTEGER NOT NULL REFERENCES surgeons(id),
            room_id        INTEGER REFERENCES operating_rooms(id),
            surgery_type   TEXT NOT NULL,
            scheduled_date TEXT NOT NULL,
            scheduled_time TEXT NOT NULL,
            duration_min   INTEGER DEFAULT 60,
            status         TEXT DEFAULT 'Scheduled'
                           CHECK(status IN ('Scheduled','In Progress','Completed','Cancelled')),
            priority       TEXT DEFAULT 'Normal'
                           CHECK(priority IN ('Emergency','High','Normal','Low')),
            notes          TEXT,
            created_by     INTEGER REFERENCES users(id),
            created_at     TEXT DEFAULT (datetime('now'))
        )
    """)

    # ── Surgery Equipment    ───────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS surgery_equipment (
            surgery_id   INTEGER REFERENCES surgeries(id),
            equipment_id INTEGER REFERENCES equipment(id),
            PRIMARY KEY (surgery_id, equipment_id)
        )
    """)

    # ── Surgery Assignments (surgery - nurse) ──────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS surgery_assignments (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            surgery_id INTEGER NOT NULL REFERENCES surgeries(id),
            nurse_id   INTEGER NOT NULL REFERENCES users(id),
            assigned_at TEXT DEFAULT (datetime('now'))
        )
    """)

    # ── Surgery Requests (surgeon - admin) ────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS surgery_requests (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            surgeon_id     INTEGER NOT NULL REFERENCES surgeons(id),
            patient_name   TEXT NOT NULL,
            surgery_type   TEXT NOT NULL,
            preferred_date TEXT NOT NULL,
            preferred_time TEXT NOT NULL,
            duration_min   INTEGER DEFAULT 60,
            priority       TEXT DEFAULT 'Normal',
            notes          TEXT,
            status         TEXT DEFAULT 'Pending'
                           CHECK(status IN ('Pending','Approved','Rejected')),
            admin_notes    TEXT,
            created_at     TEXT DEFAULT (datetime('now'))
        )
    """)

    for sql in [
        "ALTER TABLE equipment ADD COLUMN sterilized INTEGER DEFAULT 0",
        "ALTER TABLE surgeons ADD COLUMN user_id INTEGER REFERENCES users(id)",
    ]:
        try:
            c.execute(sql)
        except Exception:
            pass

    # ── Seed users ─────────────────────────────────────────────────────────
    users = [
        ("admin",    hash_password("admin123"),  "admin",   "System Administrator"),
        ("nurse1",   hash_password("nurse123"),  "nurse",   "Nurse Mehmet Faraz"),
        ("nurse2",   hash_password("nurse456"),  "nurse",   "Nurse Ali Ali"),
        ("surgeon1", hash_password("surg123"),   "surgeon", "Dr. Evgeniia Evalenko"),
        ("surgeon2", hash_password("surg456"),   "surgeon", "Dr. Ayesha Syed"),
        ("surgeon3", hash_password("surg789"), "surgeon", "Dr. Mikhail Evalenko"),
        ("surgeon4", hash_password("surg999"), "surgeon", "Dr. Diana Evalenko"),

    ]
    for u in users:
        c.execute("SELECT id FROM users WHERE username=?", (u[0],))
        if not c.fetchone():
            c.execute(
                "INSERT INTO users (username,password,role,full_name) VALUES (?,?,?,?)", u
            )

    # ── Seed surgeons ──────────────────────────────────────────────────────
    surgeons = [
        ("Dr. Mikhail Evalenko",  "Cardiothoracic",  "555-0101", "mevalenko@hospital.com"),
        ("Dr. Evgeniia Evalenko",   "Orthopedics",     "555-0102", "eevalenko@hospital.com"),
        ("Dr. Diana Evalenko", "General Surgery", "555-0104", "devalenko@hospital.com"),
        ("Dr. Ayesha Syed",      "Plastic Surgery", "555-0105", "ayesha@hospital.com"),
    ]
    for s in surgeons:
        c.execute("SELECT id FROM surgeons WHERE name=?", (s[0],))
        if not c.fetchone():
            c.execute(
                "INSERT INTO surgeons (name,specialty,phone,email) VALUES (?,?,?,?)", s
            )

    # ── Link surgeon1 - Dr. Eva, surgeon2 - Dr. Ayesha ──────
    links = [("surgeon1", "Dr. Evgeniia Evalenko"), ("surgeon2", "Dr. Ayesha Syed"),("surgeon3", "Dr. Mikhail Evalenko"),("surgeon4", "Dr. Diana Evalenko"),]
    for username, surgeon_name in links:
        c.execute("SELECT id FROM users WHERE username=?", (username,))
        u_row = c.fetchone()
        c.execute("SELECT id FROM surgeons WHERE name=?", (surgeon_name,))
        s_row = c.fetchone()
        if u_row and s_row:
            c.execute(
                "UPDATE surgeons SET user_id=? WHERE id=? AND user_id IS NULL",
                (u_row["id"], s_row["id"])
            )

    # ── Seed patients ──────────────────────────────────────────────────────
    patients = [
        ("Dexter Morgan",      "1975-03-12", "Male",   "555-1001", "A+",  "None"),
        ("Lewis Hamilton",     "1988-07-22", "Male",   "555-1002", "O-",  "Penicillin"),
        ("Rodion Raskolnikov", "1962-11-05", "Male",   "555-1003", "B+",  "Aspirin"),
        ("Tyler Durden",       "1990-01-30", "Female", "555-1004", "AB+", "None"),
        ("Walter White",       "1955-09-18", "Male",   "555-1005", "A-",  "Latex"),
    ]
    for p in patients:
        c.execute("SELECT id FROM patients WHERE name=?", (p[0],))
        if not c.fetchone():
            c.execute(
                "INSERT INTO patients (name,dob,gender,phone,blood_type,allergies) "
                "VALUES (?,?,?,?,?,?)", p
            )

    # ── Seed operating rooms ───────────────────────────────────────────────
    rooms = [
        ("OR-1", "2nd Floor"), ("OR-2", "2nd Floor"),
        ("OR-3", "3rd Floor"), ("OR-4", "3rd Floor"),
    ]
    for r in rooms:
        c.execute("SELECT id FROM operating_rooms WHERE name=?", (r[0],))
        if not c.fetchone():
            c.execute("INSERT INTO operating_rooms (name,floor) VALUES (?,?)", r)

    # ── Seed equipment ─────────────────────────────────────────────────────
    equipment = [
        ("Anesthesia Machine",   "Anesthesia",    3),
        ("Surgical Robot",       "Robotics",      1),
        ("Electrosurgical Unit", "Cauterization", 4),
        ("C-Arm Fluoroscope",    "Imaging",       2),
        ("Laparoscopic Tower",   "Laparoscopy",   2),
        ("Ventilator",           "Respiratory",   5),
    ]
    for e in equipment:
        c.execute("SELECT id FROM equipment WHERE name=?", (e[0],))
        if not c.fetchone():
            c.execute(
                "INSERT INTO equipment (name,category,quantity) VALUES (?,?,?)", e
            )

    conn.commit()
    conn.close()


# ── AUTH ───────────────────────────────────────────────────────────────────

def authenticate(username: str, password: str):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    ).fetchone()
    conn.close()
    return dict(row) if row else None


# ── SURGERIES ──────────────────────────────────────────────────────────────

def get_all_surgeries():
    conn = get_connection()
    rows = conn.execute("""
        SELECT s.*, p.name AS patient_name, sg.name AS surgeon_name,
               r.name AS room_name,
               (SELECT u.full_name FROM surgery_assignments sa
                JOIN users u ON sa.nurse_id = u.id
                WHERE sa.surgery_id = s.id LIMIT 1) AS assigned_nurse
        FROM surgeries s
        JOIN patients p  ON s.patient_id = p.id
        JOIN surgeons sg ON s.surgeon_id = sg.id
        LEFT JOIN operating_rooms r ON s.room_id = r.id
        ORDER BY s.scheduled_date, s.scheduled_time
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_surgeries_for_nurse(nurse_user_id: int):
    conn = get_connection()
    rows = conn.execute("""
        SELECT s.*, p.name AS patient_name, sg.name AS surgeon_name,
               r.name AS room_name
        FROM surgeries s
        JOIN surgery_assignments sa ON sa.surgery_id = s.id
        JOIN patients p  ON s.patient_id = p.id
        JOIN surgeons sg ON s.surgeon_id = sg.id
        LEFT JOIN operating_rooms r ON s.room_id = r.id
        WHERE sa.nurse_id = ?
        ORDER BY s.scheduled_date, s.scheduled_time
    """, (nurse_user_id,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_surgeries_for_surgeon(surgeon_user_id: int):
    conn = get_connection()
    sg = conn.execute(
        "SELECT id FROM surgeons WHERE user_id=?", (surgeon_user_id,)
    ).fetchone()
    if not sg:
        conn.close()
        return []
    rows = conn.execute("""
        SELECT s.*, p.name AS patient_name, sg.name AS surgeon_name,
               r.name AS room_name
        FROM surgeries s
        JOIN patients p  ON s.patient_id = p.id
        JOIN surgeons sg ON s.surgeon_id = sg.id
        LEFT JOIN operating_rooms r ON s.room_id = r.id
        WHERE s.surgeon_id = ?
        ORDER BY s.scheduled_date, s.scheduled_time
    """, (sg["id"],)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_surgeries_by_date(date: str):
    conn = get_connection()
    rows = conn.execute("""
        SELECT s.*, p.name AS patient_name, sg.name AS surgeon_name, r.name AS room_name
        FROM surgeries s
        JOIN patients p  ON s.patient_id = p.id
        JOIN surgeons sg ON s.surgeon_id = sg.id
        LEFT JOIN operating_rooms r ON s.room_id = r.id
        WHERE s.scheduled_date = ?
        ORDER BY s.scheduled_time
    """, (date,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def add_surgery(data: dict) -> int:
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO surgeries
          (patient_id,surgeon_id,room_id,surgery_type,scheduled_date,
           scheduled_time,duration_min,status,priority,notes,created_by)
        VALUES (:patient_id,:surgeon_id,:room_id,:surgery_type,:scheduled_date,
                :scheduled_time,:duration_min,:status,:priority,:notes,:created_by)
    """, data)
    new_id = c.lastrowid
    conn.commit()
    conn.close()
    return new_id


def assign_nurse_to_surgery(surgery_id: int, nurse_user_id: int):
    conn = get_connection()
    conn.execute("DELETE FROM surgery_assignments WHERE surgery_id=?", (surgery_id,))
    conn.execute(
        "INSERT INTO surgery_assignments (surgery_id, nurse_id) VALUES (?,?)",
        (surgery_id, nurse_user_id)
    )
    conn.commit()
    conn.close()


def get_assignment_for_surgery(surgery_id: int):
    conn = get_connection()
    row = conn.execute("""
        SELECT u.id, u.full_name FROM surgery_assignments sa
        JOIN users u ON sa.nurse_id = u.id
        WHERE sa.surgery_id = ?
    """, (surgery_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def update_surgery_status(surgery_id: int, status: str):
    conn = get_connection()
    conn.execute("UPDATE surgeries SET status=? WHERE id=?", (status, surgery_id))
    conn.commit()
    conn.close()


def delete_surgery(surgery_id: int):
    conn = get_connection()
    conn.execute("DELETE FROM surgery_equipment WHERE surgery_id=?", (surgery_id,))
    conn.execute("DELETE FROM surgery_assignments WHERE surgery_id=?", (surgery_id,))
    conn.execute("DELETE FROM surgeries WHERE id=?", (surgery_id,))
    conn.commit()
    conn.close()


# ── SURGERY REQUESTS ───────────────────────────────────────────────────────

def add_surgery_request(data: dict) -> int:
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO surgery_requests
          (surgeon_id,patient_name,surgery_type,preferred_date,preferred_time,
           duration_min,priority,notes)
        VALUES (:surgeon_id,:patient_name,:surgery_type,:preferred_date,:preferred_time,
                :duration_min,:priority,:notes)
    """, data)
    new_id = c.lastrowid
    conn.commit()
    conn.close()
    return new_id


def delete_surgery_request(request_id: int):
    """Fixed: was wrongly indented inside add_surgery_request in the original."""
    conn = get_connection()
    conn.execute("DELETE FROM surgery_requests WHERE id=?", (request_id,))
    conn.commit()
    conn.close()


def get_all_surgery_requests():
    conn = get_connection()
    rows = conn.execute("""
        SELECT sr.*, sg.name AS surgeon_name
        FROM surgery_requests sr
        JOIN surgeons sg ON sr.surgeon_id = sg.id
        ORDER BY sr.created_at DESC
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_surgery_requests_for_surgeon(surgeon_user_id: int):
    conn = get_connection()
    sg = conn.execute(
        "SELECT id FROM surgeons WHERE user_id=?", (surgeon_user_id,)
    ).fetchone()
    if not sg:
        conn.close()
        return []
    rows = conn.execute("""
        SELECT * FROM surgery_requests WHERE surgeon_id=?
        ORDER BY created_at DESC
    """, (sg["id"],)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_surgery_request_status(request_id: int, status: str, admin_notes: str = ""):
    conn = get_connection()
    conn.execute(
        "UPDATE surgery_requests SET status=?, admin_notes=? WHERE id=?",
        (status, admin_notes, request_id)
    )

    if status == "Approved":
        req = conn.execute("""
            SELECT sr.*, sg.user_id
            FROM surgery_requests sr
            JOIN surgeons sg ON sr.surgeon_id = sg.id
            WHERE sr.id = ?
        """, (request_id,)).fetchone()

        if req:
            patient = conn.execute(
                "SELECT id FROM patients WHERE name=?", (req["patient_name"],)
            ).fetchone()

            if patient:
                patient_id = patient["id"]
            else:
                c = conn.cursor()
                c.execute("INSERT INTO patients (name) VALUES (?)", (req["patient_name"],))
                patient_id = c.lastrowid

            conn.execute("""
                INSERT INTO surgeries
                (patient_id, surgeon_id, surgery_type, scheduled_date, scheduled_time,
                 duration_min, status, priority, notes)
                VALUES (?, ?, ?, ?, ?, ?, 'Scheduled', ?, ?)
            """, (
                patient_id,
                req["surgeon_id"],
                req["surgery_type"],
                req["preferred_date"],
                req["preferred_time"],
                req["duration_min"],
                req["priority"],
                req["notes"] or ""
            ))

    conn.commit()
    conn.close()


# ── SURGEON ↔ USER LINKING ─────────────────────────────────────────────────

def link_surgeon_to_user(surgeon_id: int, user_id: int):
    """
    Write user_id into the surgeons row so get_surgeries_for_surgeon() works.
    Safe to call on existing surgeons — only updates the link field.
    """
    conn = get_connection()
    conn.execute(
        "UPDATE surgeons SET user_id=? WHERE id=?", (user_id, surgeon_id)
    )
    conn.commit()
    conn.close()


def get_unlinked_surgeons():
    """Return surgeon records that have no login account linked yet."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, name FROM surgeons WHERE user_id IS NULL ORDER BY name"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_surgeon_users():
    """Return all user accounts that have the surgeon role."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, full_name FROM users WHERE role='surgeon' ORDER BY full_name"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ── PATIENTS ───────────────────────────────────────────────────────────────

def get_all_patients():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM patients ORDER BY name").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def add_patient(data: dict) -> int:
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO patients (name,dob,gender,phone,blood_type,allergies,notes)
        VALUES (:name,:dob,:gender,:phone,:blood_type,:allergies,:notes)
    """, data)
    new_id = c.lastrowid
    conn.commit()
    conn.close()
    return new_id


def update_patient(data: dict):
    conn = get_connection()
    conn.execute("""
        UPDATE patients SET name=:name, dob=:dob, gender=:gender,
          phone=:phone, blood_type=:blood_type, allergies=:allergies, notes=:notes
        WHERE id=:id
    """, data)
    conn.commit()
    conn.close()


def delete_patient(patient_id: int):
    conn = get_connection()
    conn.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    conn.close()


# ── SURGEONS ───────────────────────────────────────────────────────────────

def get_all_surgeons():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM surgeons ORDER BY name").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def add_surgeon(data: dict) -> int:
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO surgeons (name,specialty,phone,email,available)
        VALUES (:name,:specialty,:phone,:email,:available)
    """, data)
    new_id = c.lastrowid
    conn.commit()
    conn.close()
    return new_id


def update_surgeon(data: dict):
    conn = get_connection()
    conn.execute("""
        UPDATE surgeons SET name=:name, specialty=:specialty,
          phone=:phone, email=:email, available=:available
        WHERE id=:id
    """, data)
    conn.commit()
    conn.close()


def delete_surgeon(surgeon_id: int):
    conn = get_connection()
    conn.execute("UPDATE surgeons SET user_id=NULL WHERE id=?", (surgeon_id,))
    has_surgeries = conn.execute(
        "SELECT COUNT(*) FROM surgeries WHERE surgeon_id=?", (surgeon_id,)
    ).fetchone()[0]
    if has_surgeries:
        conn.close()
        raise Exception("Cannot delete surgeon — they have surgeries on record. Remove or reassign those surgeries first.")
    conn.execute("DELETE FROM surgery_requests WHERE surgeon_id=?", (surgeon_id,))
    conn.execute("DELETE FROM surgeons WHERE id=?", (surgeon_id,))
    conn.commit()
    conn.close()


# ── EQUIPMENT ──────────────────────────────────────────────────────────────

def get_all_equipment():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM equipment ORDER BY name").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_equipment_availability(eq_id: int, available: int):
    conn = get_connection()
    conn.execute("UPDATE equipment SET available=? WHERE id=?", (available, eq_id))
    conn.commit()
    conn.close()


def update_equipment_sterilized(eq_id: int, sterilized: int):
    conn = get_connection()
    conn.execute("UPDATE equipment SET sterilized=? WHERE id=?", (sterilized, eq_id))
    conn.commit()
    conn.close()


# ── USERS ──────────────────────────────────────────────────────────────────

def get_all_users():
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, username, role, full_name, created_at FROM users ORDER BY full_name"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_all_nurses():
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, full_name FROM users WHERE role='nurse' ORDER BY full_name"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def add_user(data: dict) -> int:
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO users (username, password, role, full_name)
        VALUES (:username, :password, :role, :full_name)
    """, {**data, "password": hash_password(data["password"])})
    new_id = c.lastrowid
    conn.commit()
    conn.close()
    return new_id


def delete_user(user_id: int):
    conn = get_connection()
    # Unlink from surgeon record if linked, rather than leaving a dangling user_id
    conn.execute(
        "UPDATE surgeons SET user_id=NULL WHERE user_id=?", (user_id,)
    )
    conn.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()


# ── REPORTING DATA ─────────────────────────────────────────────────────────

def get_surgeries_stats():
    conn = get_connection()
    stats = {}
    stats["by_status"] = dict(conn.execute(
        "SELECT status, COUNT(*) FROM surgeries GROUP BY status"
    ).fetchall())
    stats["by_priority"] = dict(conn.execute(
        "SELECT priority, COUNT(*) FROM surgeries GROUP BY priority"
    ).fetchall())
    stats["by_surgeon"] = conn.execute("""
        SELECT sg.name, COUNT(*) AS total
        FROM surgeries s JOIN surgeons sg ON s.surgeon_id=sg.id
        GROUP BY sg.name ORDER BY total DESC
    """).fetchall()
    stats["by_month"] = conn.execute("""
        SELECT strftime('%Y-%m', scheduled_date) AS month, COUNT(*) AS total
        FROM surgeries GROUP BY month ORDER BY month
    """).fetchall()
    stats["by_type"] = conn.execute("""
        SELECT surgery_type, COUNT(*) AS total
        FROM surgeries GROUP BY surgery_type ORDER BY total DESC LIMIT 10
    """).fetchall()
    conn.close()
    return stats


def get_all_surgeries_df_data():
    return get_all_surgeries()