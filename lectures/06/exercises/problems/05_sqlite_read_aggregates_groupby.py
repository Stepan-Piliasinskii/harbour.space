"""Problem 05: Basic aggregates and GROUP BY.

Task:
1. Count all students
2. Compute average age
3. Compute min and max age
4. Count students per track (GROUP BY track)

Print each result.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO: SELECT COUNT(*) FROM students
    cur.execute("SELECT COUNT(*) FROM students")
    count = cur.fetchone()[0]
    print(f"Total students: {count}")

    # TODO: SELECT AVG(age) FROM students
    cur.execute("SELECT AVG(age) FROM students")
    avg_age = cur.fetchone()[0]
    print(f"Average age: {avg_age:.2f}")

    # TODO: SELECT MIN(age), MAX(age) FROM students
    cur.execute("SELECT MIN(age), MAX(age) FROM students")
    min_age, max_age = cur.fetchone()
    print(f"Min age: {min_age}, Max age: {max_age}")

    # TODO: SELECT track, COUNT(*) FROM students GROUP BY track
    print("\nStudents per track:")
    cur.execute("SELECT track, COUNT(*) FROM students GROUP BY track")
    for track, count in cur.fetchall():
        print(f"{track}: {count}")

    conn.close()


if __name__ == "__main__":
    main()
