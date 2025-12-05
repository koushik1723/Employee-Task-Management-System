from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Azure SQL Connection
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://employeemanagement:%233Hfe5awcjk@employeeetaskmanagement.database.windows.net:1433/employeedb?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency: get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
