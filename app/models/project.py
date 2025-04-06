from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    jira_id = Column(String, nullable=True)
