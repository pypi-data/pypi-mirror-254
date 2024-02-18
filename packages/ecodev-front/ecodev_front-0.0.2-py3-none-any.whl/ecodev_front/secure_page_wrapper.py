"""
Module implementing a generic page wrapper to handle authentication
"""
from typing import Dict
from typing import List
from typing import Union

import dash_mantine_components as dmc
from dash import html
from ecodev_core import AppUser
from ecodev_core import get_access_token
from ecodev_core import get_user
from ecodev_core import Permission
from fastapi import HTTPException

NOT_AUTHORIZED = [html.P('Unauthorized. Please login to access')]


def safe_get_user(token: Dict) -> Union[AppUser, None]:
    """
    Safe method returning a user if one found given the passed token
    """
    try:
        return get_user(get_access_token(token))
    except (HTTPException, AttributeError):
        return None


def generic_page(token: Dict,
                 page: Union[dmc.Stack, List],
                 admin: bool = False) -> Union[dmc.Stack, List]:
    """
    Returns a NOT_AUTHORIZED if the token is not filled or if the user is not authorized to connect.

    If admin is True, the client is only authorized to connect if he has admin privileges.
    """
    if not (user := get_user(get_access_token(token))):
        return NOT_AUTHORIZED

    return page if (not admin or user.permission == Permission.ADMIN) else NOT_AUTHORIZED
