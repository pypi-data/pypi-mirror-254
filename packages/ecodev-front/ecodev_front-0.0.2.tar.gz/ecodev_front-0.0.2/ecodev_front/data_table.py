"""
Module implementing a generic Dash AG Grid table
"""
from typing import Any
from typing import Dict
from typing import List

import dash_ag_grid as dag
import pandas as pd
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class DashAgGridEnterprise(BaseSettings):
    """
    Simple authentication configuration class
    """
    dag_license_key: str = ''
    enable_dag_enterprise: bool = False
    model_config = SettingsConfigDict(env_file='.env')


DAG_ENTERPRISE_AUTH = DashAgGridEnterprise()


def data_table(id: str,
               df: pd.DataFrame,
               column_defs: List[Dict[Any, Any]] = None,
               default_col_def: Dict = None,
               style: Dict = None,
               row_alternating_color='#f5f5f5',
               row_style: Dict = None,
               dashGridOptions: Dict = None
               ) -> dag.AgGrid:
    """
    Generic Dash AG Grid table
    """
    column_defs = column_defs or [
        {'field': col, 'headerName': col.replace('_', ' ').title()} for col in df.columns]
    style = style
    default_col_def = default_col_def or {
        # make every column use 'text' filter by default
        'filter': 'agTextColumnFilter',
        # enable floating filters by default
        'floatingFilter': True,
        # make columns resizable
        'resizable': True,
        'sortable': True,
        'wrapHeaderText': True,
        'autoHeaderHeight': True,
        'wrapText': True,
        'autoHeight': True,
        # Make columns editable
        'editable': True
    }
    row_style = row_style or {
        'styleConditions': [
            {
                'condition': 'params.node.rowIndex % 2 === 1',
                'style': {'backgroundColor': row_alternating_color},
            },
        ]
    }

    dashGridOptions = dashGridOptions or {
        'colResizeDefault': 'shift',
        'rowSelection': 'single',
        'headerHeight': 30,
        'groupHeaderHeight': 30,
    }

    return dag.AgGrid(
        id=id,
        enableEnterpriseModules=DAG_ENTERPRISE_AUTH.enable_dag_enterprise,
        licenseKey=DAG_ENTERPRISE_AUTH.dag_license_key,
        columnDefs=column_defs,
        rowData=df.to_dict('records'),
        defaultColDef=default_col_def,
        style=style,
        getRowStyle=row_style,
        columnSize='responsiveSizeToFit',
        dashGridOptions=dashGridOptions
    )
