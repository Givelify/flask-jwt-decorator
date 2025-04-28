from abc import ABC, abstractmethod
from typing import Optional

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

from flask_jwt_middleware.parsed_token import ParsedToken


class TokenParser(ABC):
    @abstractmethod
    def parse(self, token: str) -> ParsedToken:
        pass


class DefaultJWTParser(TokenParser):

    # TODO we want to grab these values from some dynamic config on client part
    def __init__(self, secret_key: str, algorithms: list[str] = ["HS256"]):
        self.secret_key = secret_key
        self.algorithms = algorithms

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
