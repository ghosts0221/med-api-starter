from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "med-api-starter"
    sqlite_db_path: str = "app.db"


settings = Settings()
