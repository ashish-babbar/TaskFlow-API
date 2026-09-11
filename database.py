from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# In production this would point to Postgres, e.g.:
# postgresql://user:password@localhost:5432/taskdb
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tasks.db")

connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency that yields a DB session and guarantees it's closed."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
