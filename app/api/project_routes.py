from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.task import Task
from app.schemas.project import ProjectCreate
from app.schemas.task import TaskCreate
from app.db.deps import get_db
from app.auth.jwt_bearer import JWTBearer

router = APIRouter(dependencies=[Depends(JWTBearer())])

@router.post("/createproject")
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):
    project = Project(**data.dict())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

@router.post("/jira/createproject")
async def create_project_jira(data: ProjectCreate, db: Session = Depends(get_db)):
    from app.services.jira_service import create_jira_project
    jira_response = await create_jira_project(data.name, data.description)
    project = Project(name=data.name, description=data.description, jira_id=jira_response.get("id"))
    db.add(project)
    db.commit()
    return project

@router.post("/jira/createtask")
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
    task = Task(**data.dict())
    db.add(task)
    db.commit()
    return task
