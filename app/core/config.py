from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    JIRA_API_URL: str
    JIRA_EMAIL: str
    JIRA_API_TOKEN: str

    class Config:
        env_file = ".env"

settings = Settings()
