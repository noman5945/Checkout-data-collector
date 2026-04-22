import jwt
from datetime import datetime, timedelta,timezone
from core.config import settings


class JWTService:

    def create_access_token(self, user_id: str, role: str) -> str:

        payload = {
            "user_id": user_id,
            "role": role,
            "exp": datetime.now(timezone.utc) + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        }

        token = jwt.encode(
            payload,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM
        )

        return token


    def verify_token(self, token: str) -> dict:

        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        return payload