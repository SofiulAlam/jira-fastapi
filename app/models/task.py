from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String, default="open")
    project_id = Column(Integer, ForeignKey("projects.id"))
    jira_id = Column(String, nullable=True)
