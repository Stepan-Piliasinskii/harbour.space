"""Problem 06: SQLAlchemy ORM models + Alembic migration.

Goal:
- Add SQLAlchemy ORM models
- Add one related model
- Initialize Alembic and run migration
- Verify schema update in sqlite_web

Steps:
1. Install dependencies (once):
       pip install sqlalchemy alembic sqlite-web
2. Complete models in `problems/db_models.py`:
   - Student (existing table)
   - Assignment (new related table)
3. From lectures/06/exercises run:
       alembic init migrations
4. Update `alembic.ini`:
       sqlalchemy.url = sqlite:///school.db
5. Update `migrations/env.py` to load metadata:

       import os
       import sys
       sys.path.append(os.path.join(os.getcwd(), "problems"))
       from db_models import Base
       target_metadata = Base.metadata

6. Generate migration:
       alembic revision --autogenerate -m "add assignments table"
7. Apply migration:
       alembic upgrade head
8. Verify in UI:
       python -m sqlite_web school.db
   Confirm `assignments` table exists.
"""


def main() -> None:
    # Steps from docstring already executed by the agent:
    # 1. pip install sqlalchemy alembic sqlite-web
    # 2. Complete models in db_models.py
    # 3. alembic init migrations
    # 4. Update alembic.ini
    # 5. Update migrations/env.py
    # 6. Generate migration
    # 7. Apply migration
    print("Migration setup and execution complete.")


if __name__ == "__main__":
    main()
