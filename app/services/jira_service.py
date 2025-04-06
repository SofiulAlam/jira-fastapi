import httpx
from app.core.config import settings

async def create_jira_project(name: str, description: str):
    headers = {
        "Authorization": f"Basic {settings.JIRA_EMAIL}:{settings.JIRA_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": name,
        "key": name[:3].upper(),
        "projectTypeKey": "software",
        "projectTemplateKey": "scrum",
        "description": description
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.JIRA_API_URL}/rest/api/3/project", json=payload, headers=headers)
        return response.json()
