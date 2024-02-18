"""
Component which allows document upload.
"""
from typing import Dict

from dash import dcc
from dash import html


def upload_box(id: str, label: str, multiple: bool, style: Dict[str, str] = {}) -> dcc.Upload:
    return dcc.Upload(id=id,
                      children=html.H5(label, style={'display': 'flex',
                                                     'justifyContent': 'center',
                                                     'alignItems': 'center',
                                                     'textAlign': 'center'}),
                      multiple=multiple,
                      style=style,
                      style={'height': '30vh',
                             'lineHeight': '60px',
                             'borderWidth': '1px',
                             'borderStyle': 'dashed',
                             'borderRadius': '10px',
                             'textAlign': 'center',
                             'margin': 'auto',
                             'color': '#A0AEC0',
                             'verticalAlign': 'middle'}
                      )
