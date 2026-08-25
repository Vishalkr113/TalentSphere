from datetime import datetime, timedelta, timezone
from typing import Any


from jose import JWTError, jwt

from pwdlib import PasswordHash


from app.core.config import settings



# ==========================================================
# JWT Configuration
# ==========================================================


SECRET_KEY = settings.SECRET_KEY

ALGORITHM = settings.ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES = (
    settings.ACCESS_TOKEN_EXPIRE_MINUTES
)



# ==========================================================
# Password Hashing
# ==========================================================


password_hash = PasswordHash.recommended()



def hash_password(
    password: str,
) -> str:

    return password_hash.hash(password)



def verify_password(
    password: str,
    hashed_password: str,
) -> bool:

    return password_hash.verify(
        password,
        hashed_password,
    )



# ==========================================================
# Access Token
# ==========================================================


def create_access_token(
    data: dict[str, Any],
    expires_delta: timedelta | None = None,
) -> str:


    expire = (
        datetime.now(timezone.utc)
        +
        (
            expires_delta
            if expires_delta
            else timedelta(
                minutes=
                ACCESS_TOKEN_EXPIRE_MINUTES
            )
        )
    )


    payload = data.copy()


    payload.update(

        {

            "exp": expire,

            "iat":
                datetime.now(
                    timezone.utc
                ),

            "type":
                "access",

        }

    )


    return jwt.encode(

        payload,

        SECRET_KEY,

        algorithm=ALGORITHM,

    )



def decode_access_token(
    token: str,
) -> dict[str, Any] | None:


    try:


        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[
                ALGORITHM
            ],

        )


        if payload.get(
            "type"
        ) != "access":

            return None



        if not payload.get(
            "sub"
        ):

            return None



        return payload



    except JWTError:

        return None



# ==========================================================
# Password Reset Token
# ==========================================================


PASSWORD_RESET_EXPIRE_MINUTES = 15



def create_password_reset_token(
    email: str,
) -> str:



    expire = (

        datetime.now(
            timezone.utc
        )
        +
        timedelta(
            minutes=
            PASSWORD_RESET_EXPIRE_MINUTES
        )

    )


    payload = {


        "sub": email,


        "purpose":
            "password_reset",


        "type":
            "reset",


        "exp":
            expire,


        "iat":
            datetime.now(
                timezone.utc
            ),

    }



    return jwt.encode(

        payload,

        SECRET_KEY,

        algorithm=ALGORITHM,

    )



def decode_password_reset_token(
    token: str,
) -> str | None:


    try:


        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[
                ALGORITHM
            ],

        )


        if payload.get(
            "purpose"
        ) != "password_reset":

            return None



        if payload.get(
            "type"
        ) != "reset":

            return None



        email = payload.get(
            "sub"
        )


        if not isinstance(
            email,
            str,
        ):

            return None



        return email



    except JWTError:

        return None