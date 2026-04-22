from .interfaces.auth_services import IAuthServices
from .interfaces.user_repository import IUserRepository
from shared.auth.jwt import JWTService

class AuthenticateService(IAuthServices):
    def __init__(self,user_repo:IUserRepository):
        self.user_repo=user_repo
        self.jwtServices=JWTService()
    
    async def login(self,email:str,password:str)->str:
        """
        Steps:
        1. Take email and password
        2. Check if user exists
            - If not exists -> raise "User not found"
        3. Verify password
            - If invalid -> raise "Invalid credentials"
        4. Check if user is active or not
            - If inactive -> raise "User account is not active anymore"
        5. Generate JWT token
        6. Return token
        """
        return "token"
    
    async def updatePassword(self, user_id: str, oldPassword: str, newPassword: str) -> bool:
        return True
    
    async def logout(self) -> None:
        pass
    