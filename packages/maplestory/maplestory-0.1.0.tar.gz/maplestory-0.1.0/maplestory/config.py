from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    key: str  # API Key
    url: str = "https://open.api.nexon.com"
    timeout: int = 5000

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        env_file=".env",
        env_prefix="MAPLESTORY_OPENAPI_",
        extra="ignore",
    )
