from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import HTMLResponse
from typing import Optional

from .models.user import User
from .schemas.token import Token
from .schemas.user import UserOut, UserIn, Login
from .schemas.oauth import ResponseTypeEnum
from schemas import Detail

from .utils import create_access_token, get_password_hash
from .utils.register import send_confirmation_email
from dependencies.auth import get_current_user

from templates import templates

router = APIRouter(tags=["auth"])


@router.post(
    '/login',
    response_model=Token,
    responses={401: {'description': "Incorrect username or password"}}
)
def token(form_data: Login) -> Token:
    """
    login view
    """
    user = User.authenticate(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username, "scopes": ['me']}
    )
    return Token(**{"access_token": access_token, "token_type": "bearer"})


@router.post('/register', response_model=Token)
def register(user: UserIn) -> Token:
    """
    create a new account
    """
    user = User.create(
        username=user.username,
        hashed_password=get_password_hash(user.password),
        email=user.email
    )
    access_token = create_access_token(
        data={"sub": user.username, "scopes": ["me"]}
    )
    send_confirmation_email(user)
    return Token(**{"access_token": access_token, "token_type": "bearer"})


@router.get(
    '/me',
    response_model=UserOut,
    responses={401: {'model': Detail}},
    name="current user"
)
def me(current_user: User = get_current_user(scopes=['me'])):
    """
    get the current user
    """
    return current_user


@router.get(
    '/oauth/authorize',
    response_class=HTMLResponse
)
def oauth_authorize(
        client_id: str,
        redirect_uri: str,
        response_type: ResponseTypeEnum,
        scope: Optional[str],
        request: Request
):
    return templates.TemplateResponse("oauth/authorize.html", {'client_id': client_id, 'request': request})
