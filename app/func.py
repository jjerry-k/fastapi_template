import os
import logging

import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from typing import Annotated

if not os.path.exists("logs"):
    os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename=f'logs/api.log', level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')


def load_route(app):
    import routes
    route_path = "routes"
    route_list = os.listdir(route_path)
    for route in route_list:
        try:
            module = getattr(routes, route)
            if hasattr(module, 'router'):
                app.include_router(getattr(module, 'router'))
        except AttributeError:
            pass

security = HTTPBasic()

def check_credential(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"test"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"test"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True