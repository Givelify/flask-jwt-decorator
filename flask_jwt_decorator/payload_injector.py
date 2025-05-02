from abc import ABC, abstractmethod
from typing import Any

from flask_jwt_decorator.parsed_token import ParsedToken



class PayloadInjector(ABC):
    @abstractmethod
    def inject(self, payload: dict, request) -> None:
        pass


class DefaultPayloadInjector(PayloadInjector):
    def inject(self, payload: ParsedToken, request) -> None:
        #TODO - consult php if its doing anything by default.
        # Consumers of this library should definitely be creating their own
        # Payload injector for passing user into request object
        pass