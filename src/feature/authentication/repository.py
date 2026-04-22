from feature.authentication.model import User
from feature.authentication.interfaces.user_repository import IUserRepository

class UserRepository(IUserRepository):

    async def get_user_by_email(self, email: str) -> User | None:

        # dummy DB data (replace later with real DB)
        dummy_db = {
            "test@gmail.com": {
                "user_id": "1",
                "user_email": "test@gmail.com",
                "user_type": "admin",
                "password": "$2b$hashedpassword"
            }
        }

        user_data = dummy_db.get(email)

        if not user_data:
            return None

        # convert dict → User model
        return User(**user_data)
    
    async def get_user_by_id(self, user_id: str) -> User | None:
        pass

    async def update_password(self, user_id: str, password: str) -> None:
        pass
    
