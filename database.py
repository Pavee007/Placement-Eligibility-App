import sqlite3
import pandas as pd

class DatabaseHandler:
    def __init__(self, db_path="placement.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def fetch_eligible_students(self, min_problems=0, min_soft_skills=0):
        query = f"""
        SELECT s.student_id, s.name, s.course_batch, p.problems_solved,
               ss.communication, ss.teamwork, ss.presentation, pl.placement_status
        FROM students s
        JOIN programming p ON s.student_id = p.student_id
        JOIN soft_skills ss ON s.student_id = ss.student_id
        JOIN placements pl ON s.student_id = pl.student_id
        WHERE p.problems_solved >= ?
        AND ((ss.communication + ss.teamwork + ss.presentation + ss.leadership + ss.critical_thinking + ss.interpersonal_skills)/6) >= ?
        """
        with self.connect() as conn:
            return pd.read_sql_query(query, conn, params=(min_problems, min_soft_skills))

    def run_query(self, query: str):
        with self.connect() as conn:
            return pd.read_sql_query(query, conn)
