from dash import html
from amplabs.components import navbar, graph, selectionBar
from amplabs.variables import *

def setup_layout():
    return html.Div(
        [
            navbar.HTML_NAVBAR,
            selectionBar.htmlSelectionBar(data_names, list_of_headers),
            graph.HTML_GRAPH,
        ],
        style={"fontSize": "14px"},
    )