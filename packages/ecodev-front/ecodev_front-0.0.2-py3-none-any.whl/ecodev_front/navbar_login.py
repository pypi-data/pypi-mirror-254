"""
Module implementing the navbar login / logout components
"""
import dash_mantine_components as dmc
from dash import callback
from dash import Input
from dash import no_update
from dash import Output
from dash import State
from dash.exceptions import PreventUpdate
from ecodev_core import attempt_to_log
from ecodev_core import engine
from ecodev_core import logger_get
from fastapi import HTTPException
from sqlmodel import Session

from ecodev_front.component_ids import LOGIN_BTN_ID
from ecodev_front.component_ids import LOGIN_PASSWORD_INPUT_ID
from ecodev_front.component_ids import LOGIN_USERNAME_INPUT_ID
from ecodev_front.component_ids import LOGOUT_BTN_ID
from ecodev_front.component_ids import TOKEN
from ecodev_front.component_ids import URL

log = logger_get(__name__)


def navbar_login(username_placeholder: str = 'Username',
                 password_placeholder: str = 'Password',
                 button_label: str = 'Login',
                 button_color: str = 'white'):
    """
    Login bar component, shown when no user-tokens have been set.
    """
    return dmc.Col(span=8, children=[
        dmc.Group([
            dmc.TextInput(id=LOGIN_USERNAME_INPUT_ID,
                          placeholder=username_placeholder,
                          radius='xl',
                          style={'width': '15vw'}),
            dmc.PasswordInput(id=LOGIN_PASSWORD_INPUT_ID,
                              placeholder=password_placeholder,
                              radius='xl',
                              style={'width': '15vw'}),
            dmc.Button(button_label,
                       id=LOGIN_BTN_ID,
                       radius='xl',
                       variant=button_color,
                       style={'margin': '5px', 'width': '5vw', 'color': 'gray'})
        ], style={'display': 'flex',
                  'justifyContent': 'center',
                  'alignItems': 'center',
                  'textAlign': 'center'})
    ])


@callback(Output(TOKEN, 'data', allow_duplicate=True),
          Input(LOGIN_BTN_ID, 'n_clicks'),
          State(LOGIN_USERNAME_INPUT_ID, 'value'),
          State(LOGIN_PASSWORD_INPUT_ID, 'value'),
          prevent_initial_call=True)
def user_login(n_clicks: int, username: str, password: str):
    """
    Callback when user presses the login button.

    NB: using an attempt_to_log variation from ecodev_core to avoid
    raising an error on server-side, but rather on client-side.
    """
    if not n_clicks:
        raise no_update
    try:
        with Session(engine) as session:
            token = attempt_to_log(username, password, session)
        return {TOKEN: token}
    except HTTPException:
        return {TOKEN: {}}


@callback(
    Output(TOKEN, 'data', allow_duplicate=True),
    Output(URL, 'pathname', allow_duplicate=True),
    Input(LOGOUT_BTN_ID, 'n_clicks'),
    prevent_initial_call=True
)
def user_logout(n_clicks: int):
    """
    Reset token value when user logs out.
    """
    if not n_clicks:
        raise PreventUpdate
    return {TOKEN: None}, '/'
