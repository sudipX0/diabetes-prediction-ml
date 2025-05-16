# dpred/config.py

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    dataset_path: Path
    model_path: Path

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
