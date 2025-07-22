def queries():
    return {
        "Average Programming Performance per Batch": """
            SELECT s.course_batch, AVG(p.problems_solved) AS avg_problems
            FROM students s
            JOIN programming p ON s.student_id = p.student_id
            GROUP BY s.course_batch;
        """,
        "Top 5 Students Ready for Placement": """
            SELECT s.name, p.problems_solved, ss.communication, pl.placement_status
            FROM students s
            JOIN programming p ON s.student_id = p.student_id
            JOIN soft_skills ss ON s.student_id = ss.student_id
            JOIN placements pl ON s.student_id = pl.student_id
            WHERE pl.placement_status = 'Ready'
            ORDER BY p.problems_solved DESC
            LIMIT 5;
        """,
        "Soft Skills Score Distribution": """
            SELECT communication, teamwork, presentation, leadership,
                   critical_thinking, interpersonal_skills
            FROM soft_skills;
        """,
        "Placement Readiness Count": """
            SELECT placement_status, COUNT(*) as count
            FROM placements
            GROUP BY placement_status;
        """,
        "Internships vs Placement Status": """
            SELECT internships_completed, placement_status, COUNT(*) as count
            FROM placements
            GROUP BY internships_completed, placement_status;
        """,
        "Top Interview Performers": """
            SELECT s.name, pl.mock_interview_score
            FROM students s
            JOIN placements pl ON s.student_id = pl.student_id
            ORDER BY pl.mock_interview_score DESC
            LIMIT 5;
        """,
        "City-wise Student Count": """
            SELECT city, COUNT(*) as count
            FROM students
            GROUP BY city;
        """,
        "Certifications Earned by Students": """
            SELECT certifications_earned, COUNT(*) as count
            FROM programming
            GROUP BY certifications_earned;
        """,
        "Average Soft Skills Score by Batch": """
            SELECT s.course_batch, AVG((ss.communication + ss.teamwork + ss.presentation +
                                         ss.leadership + ss.critical_thinking + ss.interpersonal_skills)/6) AS avg_soft_skills
            FROM students s
            JOIN soft_skills ss ON s.student_id = ss.student_id
            GROUP BY s.course_batch;
        """,
        "Placed Students and Companies": """
            SELECT s.name, pl.company_name, pl.placement_package
            FROM students s
            JOIN placements pl ON s.student_id = pl.student_id
            WHERE pl.placement_status = 'Placed';
        """
    }
