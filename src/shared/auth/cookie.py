from fastapi import Response


class CookieService:

    COOKIE_NAME = "access_token"

    def set_auth_cookie(self, response: Response, token: str):

        response.set_cookie(
            key=self.COOKIE_NAME,
            value=token,
            httponly=True,
            secure=True,
            samesite="lax",
            max_age=60 * 15  # 15 min
        )


    def clear_auth_cookie(self, response: Response):

        response.delete_cookie(self.COOKIE_NAME)