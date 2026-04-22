from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from core.config import settings


# Engine with connection pooling
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=5,          # number of connections to keep
    max_overflow=10,      # extra connections
    pool_pre_ping=True,   # check connection health
    connect_args={
        "sslmode": "require"
    }
)


# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base model
Base = declarative_base()


# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()