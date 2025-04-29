from abc import ABC, abstractmethod

import jwt
from flask import current_app
from jwt import ExpiredSignatureError, InvalidTokenError

from flask_jwt_decorator.parsed_token import ParsedToken


class TokenParser(ABC):
    @abstractmethod
    def parse(self, token: str) -> ParsedToken:
        pass


class DefaultJWTParser(TokenParser):

    def __init__(self):
        self.secret_key = current_app.config["JWT_SECRET_KEY"]
        if not self.secret_key:
            raise ValueError("JWT_SECRET_KEY is required in the configuration")
        self.algorithms = current_app.config.get("JWT_ALGORITHMS", ["HS256"])

    def parse(self, token: str) -> ParsedToken:
        try:
            claims = jwt.decode(
                token,
                self.secret_key,
                algorithms=self.algorithms,
                options={
                    "verify_exp": True,
                    "verify_nbf": True,
                    "verify_iat": False,
                },
            )
            return ParsedToken(claims)
        except ExpiredSignatureError:
            raise Exception("Token has expired")
        except InvalidTokenError:
            raise Exception("Invalid token")
