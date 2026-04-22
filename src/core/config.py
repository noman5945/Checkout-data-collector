import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    def __init__(self):
        self.JWT_SECRET_KEY: str = os.getenv("JWT_SECRET") or self._raise_missing("JWT_SECRET")
        self.JWT_ALGORITHM: str = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
        self.DATABASE_URL: str = os.getenv("DATABASE_URL") or self._raise_missing("DATABASE CONNECTION URL MISSING")
        

    def _raise_missing(self, key: str) -> str:
        raise ValueError(f"{key} not set")


settings = Settings()