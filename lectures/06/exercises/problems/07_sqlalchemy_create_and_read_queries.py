"""Problem 07: Create and read data with SQLAlchemy.

Task:
1. Open a SQLAlchemy Session on `school.db`.
2. Create one Assignment for an existing student.
3. Read all students.
4. Read students with age >= 22 sorted by age descending.
5. Read assignments with joined student names.

Starter:
- Reuse `Student` and `Assignment` from `db_models.py`.
- Use `select(...)` queries.
"""

import os
import sys

# Ensure db_models can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine, select, desc
from sqlalchemy.orm import Session
from db_models import Assignment, Student

DB_URL = "sqlite:///school.db"


def main() -> None:
    engine = create_engine(DB_URL, echo=False)

    with Session(engine) as session:
        # TODO 1: add an assignment for an existing student
        # Let's pick student with id 1 (Ana)
        student_ana = session.get(Student, 1)
        if student_ana:
            # Check if assignment already exists to make it idempotent
            existing = session.scalar(select(Assignment).where(Assignment.title == "Lecture 06 Quiz", Assignment.student_id == 1))
            if not existing:
                new_assignment = Assignment(
                    title="Lecture 06 Quiz",
                    score=95,
                    student=student_ana
                )
                session.add(new_assignment)
                print(f"Added assignment for {student_ana.name}")
            else:
                print(f"Assignment for {student_ana.name} already exists.")

        # TODO 2: read all students
        print("\nAll students via ORM:")
        students = session.scalars(select(Student)).all()
        for s in students:
            print(f"{s.id}: {s.name} ({s.age}), {s.track}")

        # TODO 3: read filtered + sorted students
        print("\nStudents age >= 22 sorted by age DESC:")
        stmt = select(Student).where(Student.age >= 22).order_by(desc(Student.age))
        filtered_students = session.scalars(stmt).all()
        for s in filtered_students:
            print(f"{s.name}: {s.age}")

        # TODO 4: read assignments with student data
        print("\nAssignments with student names:")
        stmt = select(Assignment)
        assignments = session.scalars(stmt).all()
        for a in assignments:
            print(f"Assignment: {a.title}, Score: {a.score}, Student: {a.student.name}")

        session.commit()


if __name__ == "__main__":
    main()
