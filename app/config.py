import os
from dataclasses import dataclass
@dataclass(frozen=True)
class Settings:
    api_token:str=os.getenv("HAZARDHALO_API_TOKEN", "")
    database_url:str=os.getenv("HAZARDHALO_DATABASE_URL", "sqlite:///./data/hazardhalo.db")
    demo_mode:bool=os.getenv("HAZARDHALO_DEMO_MODE", "false").lower()=="true"
settings=Settings()
