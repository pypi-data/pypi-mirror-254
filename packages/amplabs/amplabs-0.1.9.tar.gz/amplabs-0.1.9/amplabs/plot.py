from dash import Dash, Input, Output, State, ALL
import plotly.io as pio
import dash_bootstrap_components as dbc
import sys
from amplabs.components.appLayout import setup_layout
from amplabs.variables import *
import amplabs.variables as avs
from amplabs.callbacks.toggleNavbar import toggle_navbar_collapse
from amplabs.callbacks.updateLineChart import update_line_chart
import platform

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


if platform.system() == 'Darwin':
    pio.renderers.default = 'svg'


class plot:
    instances = []

    def __init__(self, df, df_name=None, x_columns=None, y_columns=None):
        try:
            self.df = df
            self.df_name = df_name
            self.xcolumn = x_columns
            self.ycolumn = y_columns
            self.headers = self.df.columns.tolist()
            plot.instances.append(self)
        except TypeError as dfe:
            print(f"Error: {dfe}")
            sys.exit(1)

    def set_color(self, colors):
        self.colors = colors

    def set_xrange(self, ranges):
        self.xrange = ranges

    def set_yrange(self, ranges):
        self.yrange = ranges

    def set_xintervals(self, intervals):
        self.xinterval = intervals

    def set_yintervals(self, intervals):
        self.yinterval = intervals

    def set_xlabel(self, label):
        self.xlabel = label

    def set_ylabel(self, label):
        self.ylabel = label

    def set_linewidth(self, width):
        try:
            # Show an error when you receive a string here
            if not isinstance(width, (int, float)):
                raise TypeError("Width must be an int or float")
            self.line_width = width
        except TypeError as ve:
            print(f"Error:{ve}")
            sys.exit(1)

    @classmethod
    def reset_all(cls):
        #Clear the instance 
        cls.instances = []
        # Clear global variables
        data_list.clear()
        list_of_headers.clear()
        color_list.clear()
        x_ranges.clear()
        y_ranges.clear()
        x_interval.clear()
        y_interval.clear()
        line_width.clear()
        ylabel.clear()
        x_columns.clear()
        y_columns.clear()        

    @classmethod
    def plot_on_dashboard(cls):
        for instance in cls.instances:
            data_list.append(instance.df)
            data_names.append(instance.df_name)
            list_of_headers.append(instance.headers)
            color_list.append(getattr(instance, "colors", []))
            x_ranges.append(getattr(instance, "xrange", []))
            y_ranges.append(getattr(instance, "yrange", []))
            x_interval.append(getattr(instance, "xinterval", []))
            y_interval.append(getattr(instance, "yinterval", []))
            line_width.append(getattr(instance, "line_width", 2.5))
            ylabel.append(getattr(instance, "ylabel", None))
            avs.xlabel = (
                getattr(instance, "xlabel", None)
                if isinstance(getattr(instance, "xlabel", None), str)
                else avs.xlabel
            )
        try:
            # add callback for toggling the collapse on small screens
            app.callback(
                Output("navbar-collapse", "is_open"),
                [Input("navbar-toggler", "n_clicks")],
                [State("navbar-collapse", "is_open")],
            )(toggle_navbar_collapse)

            app.layout = setup_layout()

            app.callback(
                Output("graph", "figure"),
                [Input({"type": "add-x", "index": ALL}, "value")],
                [Input({"type": "add-y", "index": ALL}, "value")],
            )(update_line_chart)

        except ValueError as ve:
            print(f"Error: {ve}")
            sys.exit(1)
        except Exception as ve:
            print(f"Error: {ve}")
            sys.exit(1)

        start_dash_server()

    @classmethod
    def plot_as_svg(cls):
        try:
            for instance in cls.instances:
                data_list.append(instance.df)
                list_of_headers.append(instance.headers)
                color_list.append(getattr(instance, "colors", []))
                x_ranges.append(getattr(instance, "xrange", []))
                y_ranges.append(getattr(instance, "yrange", []))
                x_interval.append(getattr(instance, "xinterval", []))
                y_interval.append(getattr(instance, "yinterval", []))
                line_width.append(getattr(instance, "line_width", 2))
                ylabel.append(getattr(instance, "ylabel", None))
                avs.xlabel = (
                    getattr(instance, "xlabel", None)
                    if isinstance(getattr(instance, "xlabel", None), str)
                    else avs.xlabel
                )
                x_columns.append(instance.xcolumn)
                y_columns.append(instance.ycolumn)
            fig = update_line_chart(x_columns, y_columns)
            fig.show()
            cls.reset_all()
        except ValueError as ve:
            print(f"Error: {ve}")
            sys.exit(1)
        except Exception as ve:
            print(f"Error: {ve}")
            sys.exit(1)


def start_dash_server():
    global dash_server_running
    app.run_server(debug=True)
