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

from ecodev_front.component_ids import LOGIN_BTN_ID
from ecodev_front.component_ids import LOGIN_PASSWORD_INPUT_ID
from ecodev_front.component_ids import LOGIN_USERNAME_INPUT_ID
from ecodev_front.component_ids import TOKEN



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
