import plotly.graph_objects as go
from amplabs.variables import *
import amplabs.variables as avs
import random


def update_line_chart(x_axes, y_axes_values):
    fig = go.Figure()
    # Create y-axes for the selected traces
    for i, y_values in enumerate(y_axes_values):
        if len(y_values) == 0 or x_axes[i] == "":
            continue
        axis_num = i + 1
        df = data_list[i]
        if len(color_list[i]) == 0:
            color_list[i] = colorTransitions[i]
        if i == 0:
            for j, y_axis in enumerate(y_values):
                if j >= len(color_list[i]):
                    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                    color_list[i].append(color)
                else:
                    color = color_list[i][j]

                y_df = [float(temp) for temp in df[y_axis]]
                x_df = [float(temp) for temp in df[x_axes[i]]]
                fig.add_trace(
                    go.Scatter(
                        x=x_df,
                        y=y_df,
                        name=y_axis,
                        line=dict(color=color, width=line_width[i]),
                        showlegend=True,
                    )
                )
            fig.update_layout(
                yaxis=dict(
                    title=ylabel[i],
                    titlefont=dict(color="#ff7f0e"),
                    tickfont=dict(color="#ff7f0e"),
                    ticks="outside",
                )
            )
        else:
            for j, y_axis in enumerate(y_values):
                if j >= len(color_list[i]):
                    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                    color_list[i].append(color)
                else:
                    color = color_list[i][j]
                y_df = [float(temp) for temp in df[y_axis]]
                x_df = [float(temp) for temp in df[x_axes[i]]]
                fig.add_trace(
                    go.Scatter(
                        x=x_df,
                        y=y_df,
                        name=y_axis,
                        yaxis=f"y{axis_num}",
                        line=dict(color=color, width=line_width[i]),
                    )
                )
                fig.update_layout(
                    **{
                        f"yaxis{axis_num}": dict(
                            title=ylabel[i],
                            overlaying="y",
                            side="right",
                            titlefont=dict(color="#ff7f0e"),
                            tickfont=dict(color="#ff7f0e"),
                            autoshift=True,
                            anchor="free",
                            ticks="outside",
                            shift=20 * (i - 1),
                        )
                    }
                )
    fig.update_layout(
        dict(
            legend={"x": 1.05, "y": 0.9},
        ),
        width=1200,
        height=600,
        xaxis_title=avs.xlabel,
    )

    for i, x_range in enumerate(
        x_ranges,
    ):
        if len(x_range) == 0:
            continue
        x_axis_name = "xaxis"  # Generate unique x-axis identifier
        fig.update_layout(**{x_axis_name: dict(range=x_range)})

    for i, y_range in enumerate(
        y_ranges,
    ):
        if len(y_range) == 0:
            continue
        y_axis_name = "yaxis"
        y_num = i + 1
        if y_num != 1:
            y_axis_name = y_axis_name + str(y_num)
        fig.update_layout(
            **{
                y_axis_name: dict(
                    range=y_range,
                )
            }
        )

    for i, y_tick in enumerate(
        y_interval,
    ):
        if isinstance(y_tick, (int, float)) is False:
            continue
        y_axis_name = "yaxis"
        y_num = i + 1
        tick_num = y_tick
        if y_num != 1:
            y_axis_name = y_axis_name + str(y_num)
        fig.update_layout(
            **{
                y_axis_name: dict(
                    dtick=tick_num,
                )
            }
        )

    for i, x_tick in enumerate(
        x_interval,
    ):
        if isinstance(x_tick, (int, float)) is False:
            continue
        x_axis_name = "xaxis"
        fig.update_layout(
            **{
                x_axis_name: dict(
                    dtick=x_tick,
                )
            }
        )

    # Update layout with dynamically generated x-axes
    fig.update_xaxes(
        showline=True,
        linewidth=1,
        linecolor="black",
        mirror=True,
        ticks="outside",
    )
    fig.update_yaxes(
        showline=True,
        linewidth=1,
        linecolor="black",
        mirror=True,
        # ticks="outside",
    )
    return fig