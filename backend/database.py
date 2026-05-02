from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Your MySQL connection
password = quote_plus("Zoya.@sql7866")
DATABASE_URL = f"mysql+pymysql://root:{password}@localhost:3306/document_qa"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Documents table
class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String(255))
    filepath = Column(String(500))
    uploaded_at = Column(DateTime, default=datetime.utcnow)

# Creates table if it doesn't exist
Base.metadata.create_all(engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()