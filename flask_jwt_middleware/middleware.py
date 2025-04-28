from functools import wraps

from flask import abort, request

from flask_jwt_middleware.parser import DefaultJWTParser, TokenParser
from flask_jwt_middleware.payload_injector import (
    DefaultPayloadInjector,
    PayloadInjector,
)
from flask_jwt_middleware.validators import DefaultJWTValidator, TokenValidator


def get_auth_header_token(req):
    auth_header = req.headers.get("Authorization", None)
    if not auth_header:
        return None

    parts = auth_header.split()

    if parts[0].lower() != "bearer" or len(parts) != 2:
        return None

    return parts[1]


def token_required(
    parser: TokenParser = DefaultJWTParser(),
    validator: TokenValidator = DefaultJWTValidator(),
    payload_injector: PayloadInjector = DefaultPayloadInjector(),
):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            token = get_auth_header_token(request)
            if not token:
                abort(401, description="Missing token")

            try:
                payload = parser.parse(token)
            except Exception as e:
                abort(401, description=f"Token parsing failed: {str(e)}")

            try:
                validator.validate(payload)
            except Exception as e:
                abort(401, description=f"Token validation failed: {str(e)}")

            payload_injector.inject(payload, request)
            return f(*args, **kwargs)

        return wrapped

    return decorator
