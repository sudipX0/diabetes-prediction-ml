from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    dataset_path: Path
    model_path: Path

    class Config:
        env_file = ".env"


settings = Settings()

project_root = Path(__file__).parent.parent.resolve()

settings.dataset_path = (project_root / settings.dataset_path).resolve()
settings.model_path = (project_root / settings.model_path).resolve()
