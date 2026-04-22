from abc import ABC,abstractmethod

class IAuthServices(ABC):
    
    @abstractmethod
    async def login(self,email:str,password:str)->str:pass

    @abstractmethod
    async def updatePassword(self,user_id:str,oldPassword:str,newPassword:str)->bool:pass
    
    @abstractmethod
    async def logout(self)->None:pass