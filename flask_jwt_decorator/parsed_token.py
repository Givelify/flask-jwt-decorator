from datetime import datetime
from typing import Any, Dict, Optional


class ParsedToken:
    def __init__(self, claims: Optional[Dict[str, Any]] = None):
        self._claims = claims or {}

        self.subject = self._claims.get("sub")
        self.identifier = self._claims.get("jti")
        self.issuer = self._claims.get("iss")
        self.audience = self._claims.get("aud")

        self.expiration_time = self._parse_time("exp")
        self.issue_time = self._parse_time("iat")
        self.beginning_time = self._parse_time("nbf")

    def to_dict(self) -> Dict[str, Any]:
        return self._claims

    def get(self, claim: str, default: Any = None) -> Any:
        return self._claims.get(claim, default)

    def _parse_time(self, claim: str) -> Optional[datetime]:
        raw = self._claims.get(claim)
        value = self._format_string(raw)
        return self._format_time(value)

    def _format_string(self, value: Any) -> Optional[str]:
        if value is None:
            return None
        if isinstance(value, (str, int, float, bool)):
            return str(value)
        raise TypeError(f"Cannot cast {type(value).__name__} value to string")

    def _format_time(self, value: Optional[str]) -> Optional[datetime]:
        if value is None:
            return None
        try:
            if value.isdigit():
                return datetime.fromtimestamp(int(value))
            return datetime.fromisoformat(value)
        except Exception as e:
            raise ValueError(f"Could not parse time: {e}") from e
