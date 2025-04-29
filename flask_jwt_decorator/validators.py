from abc import ABC, abstractmethod
from typing import Any


class TokenValidator(ABC):
    @abstractmethod
    def validate(self, payload: dict) -> None:
        pass


class DefaultJWTValidator(TokenValidator):
    def validate(self, payload: dict) -> None:
        if "sub" not in payload:
            raise ValueError("Subject claim missing")
