"""
Config module for this application.
"""

import logging

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))

logging.basicConfig(level=logging.INFO)


class Settings(BaseSettings):
    EKM_DOC_RETRIEVAL_API_URL: str = ''
    APP_ID: str = ''

    # class Config:
    #     env_file = ".env"
    #     case_sensitive = True
    # model_config = SettingsConfigDict(env_file=".env")
    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()