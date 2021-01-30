from settings import AUTH as AUTH_SETTINGS, SECRET_KEY, OAUTH2_SCHEMA
from pydantic import ValidationError
from jose import jwt, JWTError
from fastapi.security import SecurityScopes
from fastapi import Depends, HTTPException, status, Security
from auth.models.user import User
from auth.schemas.token import TokenData
from typing import List, Optional


async def _get_current_user(security_scopes: SecurityScopes, token: str = Depends(OAUTH2_SCHEMA)):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=AUTH_SETTINGS['ALGORITHM'])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception
    user = User.filter(username=token_data.username)
    if user is None:
        raise credentials_exception

    if 'me' in token_data.scopes:
        return user

    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


def get_current_user(scopes: Optional[List[str]] = None):
    return Security(_get_current_user, scopes=scopes)

