from pydantic import BaseModel

class User(BaseModel):
    user_id:str
    user_email:str
    user_type:str
    password:str

class LoginRequest(BaseModel):
    userEmail:str
    password:str

class LoginResponse(BaseModel):
    message:str

class UpdatePasswordRequest(BaseModel):
    old_password: str
    new_password: str

class BasicResponse(BaseModel):
    message: str