from dash import html
import dash_bootstrap_components as dbc
from PIL import Image

import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the "assets" directory at the root of the project
project_root = os.path.abspath(os.path.join(script_dir, "../../"))
assets_dir = os.path.join(project_root, "assets")

# Construct the absolute path to the "favicon.ico" file
image_path = os.path.join(assets_dir, "favicon.png")

AMPLABS_LOGO = Image.open(image_path)


HTML_NAVBAR = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=AMPLABS_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("AmpLabs", className="ms-2")),
                ],
                align="center",
                className="g-0",
            ),
            href="https://plotly.com",
            style={"textDecoration": "none", "marginLeft": "1%"},
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        dbc.Collapse(
            dbc.Row(
                [
                    dbc.Col(
                        dbc.NavItem(
                            dbc.NavLink(
                                "About Us",
                                href="https://www.amplabs.ai/",
                                target="_blank",
                            )
                        ),
                    ),
                ],
                style={"color": "white"},
            ),
            id="navbar-collapse",
            is_open=False,
            navbar=True,
            style={
                "justifyContent": "end",
                "marginRight": "5%",
            },
        ),
    ],
    color="dark",
    dark=True,
)
