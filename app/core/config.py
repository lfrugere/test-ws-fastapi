from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    api_keys: str = Field(default="", alias="API_KEYS")

    @property
    def client_api_keys(self) -> dict[str, str]:
        clients: dict[str, str] = {}

        for item in self.api_keys.split(","):
            if not item:
                continue

            app_name, separator, api_key = item.partition(":")
            if separator and app_name and api_key:
                clients[app_name] = api_key

        return clients


@lru_cache
def get_settings() -> Settings:
    return Settings()
