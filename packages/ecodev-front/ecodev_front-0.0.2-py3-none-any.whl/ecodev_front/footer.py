"""
Dash app component to display the page footers.
"""
from dash import callback
from dash import html
from dash import Input
from dash import Output
from ecodev_core import is_authorized_user

from ecodev_front.component_ids import FOOTER
from ecodev_front.component_ids import TOKEN
from ecodev_front.component_ids import URL
from ecodev_front.secure_page_wrapper import get_access_token


def footer(children: html.Div, color: str = '#0066A1', height: str = '5vh') -> html.Div:
    """Main app footer"""
    return html.Div(children, id=FOOTER,
                    style={'position': 'fixed',
                           'bottom': 0,
                           'height': height,
                           'width': '100vw',
                           'paddingBottom': '10px',
                           'backgroundColor': color,
                           'color': 'white',
                           'display': 'flex',
                           'textAlign': 'center',
                           'alignContent': 'center',
                           'justifyContent': 'center',
                           })


@callback(
    Output(FOOTER, 'style'),
    Input(TOKEN, 'data'),
    Input(URL, 'pathname')
)
def show_hide_footer(token, pathname: str):
    """
    Navbar update. If no valid token is present in the store, return the login component.
    Otherwise, return the full navbar with all the page app.
    """
    return {'display': 'flex' if is_authorized_user(get_access_token(token)) else 'None'}
