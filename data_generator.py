import sqlite3
from faker import Faker
import random

fake = Faker()

conn = sqlite3.connect("placement.db")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS programming;
DROP TABLE IF EXISTS soft_skills;
DROP TABLE IF EXISTS placements;
""")

cursor.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    email TEXT,
    phone TEXT,
    enrollment_year INTEGER,
    course_batch TEXT,
    city TEXT,
    graduation_year INTEGER
);
""")

cursor.execute("""
CREATE TABLE programming (
    programming_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    language TEXT,
    problems_solved INTEGER,
    assessments_completed INTEGER,
    mini_projects INTEGER,
    certifications_earned INTEGER,
    latest_project_score REAL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
""")

cursor.execute("""
CREATE TABLE soft_skills (
    soft_skill_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    communication INTEGER,
    teamwork INTEGER,
    presentation INTEGER,
    leadership INTEGER,
    critical_thinking INTEGER,
    interpersonal_skills INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
""")

cursor.execute("""
CREATE TABLE placements (
    placement_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    mock_interview_score INTEGER,
    internships_completed INTEGER,
    placement_status TEXT,
    company_name TEXT,
    placement_package REAL,
    interview_rounds_cleared INTEGER,
    placement_date TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
""")

languages = ["Python", "SQL", "Java"]
statuses = ["Ready", "Not Ready", "Placed"]
companies = ["TCS", "Infosys", "Wipro", "Amazon", "Google", None]

for sid in range(1, 101):
    cursor.execute("""
        INSERT INTO students (student_id, name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        sid, fake.name(), random.randint(20, 25), random.choice(["Male", "Female", "Other"]),
        fake.email(), fake.phone_number(), random.randint(2019, 2022),
        random.choice(["Batch A", "Batch B"]), fake.city(), random.randint(2023, 2025)
    ))

    cursor.execute("""
        INSERT INTO programming (student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        sid, random.choice(languages), random.randint(10, 200), random.randint(1, 10),
        random.randint(0, 5), random.randint(0, 3), round(random.uniform(50, 100), 2)
    ))

    cursor.execute("""
        INSERT INTO soft_skills (student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        sid, *(random.randint(50, 100) for _ in range(6))
    ))

    status = random.choice(statuses)
    company = random.choice(companies) if status == "Placed" else None
    package = round(random.uniform(3, 20), 2) if company else None
    date = fake.date_this_year() if company else None

    cursor.execute("""
        INSERT INTO placements (student_id, mock_interview_score, internships_completed, placement_status, company_name, placement_package, interview_rounds_cleared, placement_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        sid, random.randint(50, 100), random.randint(0, 3), status,
        company, package, random.randint(1, 5), date
    ))

conn.commit()
conn.close()
print("Data generation complete.")
