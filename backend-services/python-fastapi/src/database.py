from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tenacity import retry, stop_after_attempt, wait_fixed

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres:5432/mydatabase"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True  # Add connection health checks
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def init_db():
    try:
        # Try to create database tables
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        raise e

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()