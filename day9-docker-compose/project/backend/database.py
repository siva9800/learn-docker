
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:12345678@localhost:5432/app_db",
)
engine = create_engine(db_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
