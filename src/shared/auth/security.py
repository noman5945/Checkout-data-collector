from fastapi import Depends, HTTPException, status
from .dependency import get_current_user


def require_role(role: str):

    def wrapper(user=Depends(get_current_user)):

        if user.get("role") != role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden"
            )

        return user

    return wrapper