from dash import dcc
import dash_bootstrap_components as dbc


def generateDropDowns(column_headers, index):
    dropdownLayout = dbc.Row(
        [
            dbc.Col(dbc.Label("X-Axis:"), width="auto"),
            dbc.Col(
                dcc.Dropdown(
                    id={"type": "add-x", "index": index},
                    options=column_headers[index],
                    value="",
                    placeholder="Select x axis",
                    style={
                        "width": "100%",
                        "display": "inline-block",
                        "alignSelf": "center",
                    },
                ),
            ),
            dbc.Col(dbc.Label("Y-Axis:"), width="auto"),
            dbc.Col(
                dcc.Dropdown(
                    id={"type": "add-y", "index": index},
                    options=column_headers[index],
                    value=[],
                    multi=True,
                    placeholder="Select y axis",
                    style={
                        "width": "100%",
                        "display": "inline-block",
                        "alignSelf": "center",
                    },
                ),
            ),
        ],
        style={
            "marginTop": "2%",
            "marginLeft": "5%",
            "alignItems": "center",
        },
    )
    return dropdownLayout


def generate_axes_selection(file_names, column_headers):
    items = []

    for index, file_path in enumerate(file_names):
        items.append(dbc.ListGroupItem(file_path.lstrip("./")))
        items.append(generateDropDowns(column_headers, index))
    return items


def htmlSelectionBar(list_of_file_names, list_of_headers):
    selectionBar = dbc.Card(
        dbc.CardBody(
            [
                dbc.ListGroup(
                    generate_axes_selection(list_of_file_names, list_of_headers),
                    numbered=True,
                    id="axes_selection",
                )
            ],
            className="w-100",
        ),
        className="mb-3 d-flex align-items-center w-100",
    )
    return selectionBar
