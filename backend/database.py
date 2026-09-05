from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_FILE = DATABASE_DIR / "academic_training.db"

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"


engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()