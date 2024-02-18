from datetime import datetime, timedelta
from typing import Any, Optional

import jwt

from quest_maker_api_shared_library.errors.authentication import ScopeError, ExpiredTokenError, InvalidTokenError


class TokenManager:
    def __init__(self,
                 key: str,
                 jwt_expiration_time_in_minutes: int,
                 algorithm: str = "HS256") -> None:
        self.key = key
        self.jwt_expiration_time_in_minutes = jwt_expiration_time_in_minutes
        self.algorithm = algorithm

    def encode_token(
            self,
            identifier: Any,
            scope="create modify:own view:own") -> str:
        payload = {
            "exp": datetime.utcnow() + timedelta(minutes=self.jwt_expiration_time_in_minutes),
            "iat": datetime.utcnow(),
            "scope": scope,
            "sub": identifier
        }
        return jwt.encode(payload=payload, key=self.key, algorithm=self.algorithm)

    def decode_token(
            self,
            token: str) -> Optional[Any]:
        try:
            payload = jwt.decode(
                jwt=token, key=self.key, algorithms=[self.algorithm])
            if payload:
                return payload
            raise ScopeError(detail=payload['scope'])
        except jwt.ExpiredSignatureError:
            raise ExpiredTokenError
        except jwt.InvalidTokenError:
            raise InvalidTokenError
