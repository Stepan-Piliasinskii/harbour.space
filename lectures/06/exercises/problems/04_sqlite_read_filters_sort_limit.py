"""Problem 04: Practice WHERE, ORDER BY, LIMIT.

Task:
1. Get students with age >= 22
2. Sort students by age DESC
3. Return only top 3 oldest students
4. Get backend students younger than 23

Use parameterized queries for filter values.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO 1: age >= 22
    print("Students with age >= 22:")
    cur.execute("SELECT * FROM students WHERE age >= ?", (22,))
    for row in cur.fetchall():
        print(row)

    # TODO 2 + 3: order by age desc, limit 3
    print("\nTop 3 oldest students:")
    cur.execute("SELECT * FROM students ORDER BY age DESC LIMIT 3")
    for row in cur.fetchall():
        print(row)

    # TODO 4: track='backend' and age < 23
    print("\nBackend students younger than 23:")
    cur.execute("SELECT * FROM students WHERE track = ? AND age < ?", ("backend", 23))
    for row in cur.fetchall():
        print(row)

    conn.close()


if __name__ == "__main__":
    main()
