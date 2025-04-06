from app.models.user import User
from app.models.project import Project
from app.models.task import Task
from app.db.database import SessionLocal
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def seed_data():
    db = SessionLocal()

    if db.query(User).first():
        db.close()
        return

    demo_user = User(username="admin", password=pwd_context.hash("admin"))
    db.add(demo_user)

    project = Project(name="Demo Project", description="A sample project")
    db.add(project)
    db.commit()
    db.refresh(project)

    task1 = Task(title="Initial Task", description="Kickoff task", project_id=project.id)
    db.add(task1)

    db.commit()
    db.close()
