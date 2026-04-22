from abc import ABC,abstractmethod
from feature.authentication.model import User

class IUserRepository(ABC):

    @abstractmethod
    async def get_user_by_email(self,email:str)->User|None:
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> User | None:
        pass

    @abstractmethod
    async def update_password(self, user_id: str, password: str) -> None:
        pass