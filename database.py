from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus  # to encode password

load_dotenv()

MYSQL_USER = os.getenv("DB_USERNAME")
MYSQL_PASSWORD = os.getenv("DB_PASSWORD")
MYSQL_HOST = os.getenv("DB_HOST")
MYSQL_PORT = os.getenv("DB_PORT")
MYSQL_DB = os.getenv("DB_NAME")

# Encode the password to make it safe for URL
if MYSQL_PASSWORD is None:
    raise ValueError("MYSQL_PASSWORD is not set. Check your .env file.")
encoded_password = quote_plus(str(MYSQL_PASSWORD))


SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{encoded_password}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
print("Loaded from .env:", MYSQL_USER, MYSQL_PASSWORD)
