from dash import dcc
import dash_bootstrap_components as dbc


HTML_GRAPH = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id="graph", style={"display": "grid", "justifyContent": "center"}
            ),
        )
    ]
)
