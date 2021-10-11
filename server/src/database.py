from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./user_database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()