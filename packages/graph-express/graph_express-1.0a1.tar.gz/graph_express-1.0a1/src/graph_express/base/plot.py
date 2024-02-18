from abc import ABCMeta
from collections import Counter
from os.path import splitext
from typing import Literal, Optional, Union

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
import seaborn as sns
from matplotlib import colormaps as cmaps
from matplotlib.colors import LinearSegmentedColormap, is_color_like

from .graph import Graph
from .layout import Layout
from ..utils import (
    method_class,
    method_input,
)

pio.templates.default = "none"

FIGSIZE = (5, 5)

DEFAULT_SIZE = 10
DEFAULT_EDGE_COLOR = "#aaa"
DEFAULT_FONT_COLOR = "black"
DEFAULT_NODE_COLOR = "#bbb"
DEFAULT_CONNECTIONSTYLE = "arc3"
DEFAULT_CONNECTIONSTYLE_CURVED = "arc3,rad=0.25"

DEFAULT_COLOR_DISCRETE = [
    "#006cb7",
    "#ff7700",
    "#00b035",
    "#ed0000",
    "#a643bd",
    "#965146",
    "#fb4cbe",
    "#7f7f7f",
    "#b2cb10",
    "#00c2d3",
]

DEFAULT_COLOR_SEQUENCE = [
    "#4e9cd5",
    "#8eb2b2",
    "#f6e16d",
    "#d47950",
    "#d11e26",
]


class Plot(metaclass=ABCMeta):

    @staticmethod
    def draw(*args, **kwargs):
        """
        Wrapper function for drawing graphs. Aliases: `draw`, `plot`.

        Available backends:
        * `nx` or `networkx` (default) -> `draw_nx`
        * `plotly` -> `draw_plotly`

        For more information, please see the listed functions above.
        """
        backend = kwargs.pop("backend", "nx")
        backend = "nx" if backend == "networkx" else backend
        return getattr(Plot, f"draw_{backend}")(*args, **kwargs)

    @staticmethod
    def draw_nx(
        G: nx.Graph,
        pos: Optional[Union[str, dict, pd.DataFrame]] = None,
        node_color: Optional[Union[str, list, dict, pd.Series, pd.DataFrame]] = None,
        node_size: Optional[Union[int, list]] = None,
        edge_color: Optional[str] = None,
        arrows: Optional[bool] = True,
        cmap: Optional[Union[str, list]] = None,
        cmap_loop: Optional[bool] = False,
        connectionstyle: Optional[str] = None,
        curved_edges: Optional[bool] = False,
        figsize: Optional[tuple] = FIGSIZE,
        font_color: Optional[str] = None,
        show: Optional[bool] = False,
        title: Optional[str] = "",
        width: Optional[float] = 0.5,
        with_labels: Optional[bool] = False,
        **kwargs
    ) -> plt.Figure:
        """
        Returns matplotlib figure from NetworkX graph.
        """
        pos = Plot._get_positions(G, pos).apply(list, axis=1).to_dict()

        fig = plt.figure(figsize=figsize)
        plt.title(title)

        # Convert node sizes to dictionary...
        if type(node_size) in (pd.Series, pd.DataFrame):
            node_size = node_size.squeeze().to_dict()

        # ...and to ordered list.
        if type(node_size) == dict:
            node_size = [node_size[node] for node in G.nodes()]

        # Convert node colors to dictionary.
        if type(node_color) in (pd.Series, pd.DataFrame):
            node_color = node_color.squeeze().to_dict()

        # Use node degrees as colors by default.
        if node_color is None or node_color is True:
            node_color = [node_degree[1] for node_degree in G.degree()]

        # Treat node colors as sequential.
        if type(node_color) == list and not is_color_like(node_color[0]):
            cmap = LinearSegmentedColormap.from_list("custom", DEFAULT_COLOR_SEQUENCE)\
                   if cmap is None else cmaps[cmap]

        # Treat node colors as discrete.
        if type(node_color) == dict:

            # Rebuild dictionary keys from groups to nodes.
            if type(node_color[list(node_color)[0]]) == list:
                node_color = {node: group
                              for group in node_color
                              for node in node_color[group]}

            # Use source node color for edges.
            # if edge_color is None:
            #     edge_color = [node_color[edge[0]] for edge in G.edges()]

            # Convert node colors to ordered list.
            if not is_color_like(node_color[list(node_color)[0]]):
                cmap = DEFAULT_COLOR_DISCRETE\
                       if cmap is None else list(cmap)

                node_color = [
                    (
                        cmap[node_color[node] % len(cmap)]
                        if node_color[node] != -1
                        and (cmap_loop or node_color[node] < len(cmap))
                        else DEFAULT_NODE_COLOR
                    )
                    if node_color.get(node) is not None else DEFAULT_NODE_COLOR
                    for node in G.nodes()
                ]

        nx.draw(G,
                pos=pos,
                node_color=node_color or DEFAULT_NODE_COLOR,
                edge_color=edge_color or DEFAULT_EDGE_COLOR,
                node_size=node_size or DEFAULT_SIZE,
                connectionstyle=connectionstyle or (DEFAULT_CONNECTIONSTYLE_CURVED if curved_edges else DEFAULT_CONNECTIONSTYLE),
                font_color=font_color or DEFAULT_FONT_COLOR,
                arrows=arrows,
                cmap=cmap,
                width=width,
                with_labels=with_labels,
                **kwargs)

        if show:
            plt.show(fig)

        plt.close(fig)

        return fig

    @staticmethod
    def draw_plotly(
        G: nx.Graph,
        pos: Optional[Union[str, dict, pd.DataFrame]] = None,
        colorbar_title: str = "",
        colorbar_thickness: int = 10,
        colorscale: Union[list, bool] = None,
        edge_color: Optional[str] = None,
        edge_width: float = 1.0,
        font_color: str = "grey",
        font_family: str = "sans-serif",
        font_size: int = 16,
        groups: dict = None,
        group_colors: list = DEFAULT_COLOR_DISCRETE,
        height: int = 1000,
        labels: dict = None,
        node_color: Union[str, dict] = None,
        node_line_color: str = "#000",
        node_line_width: float = 1.0,
        node_opacity: float = 1.0,
        node_size: Union[int, dict] = None,
        reversescale: bool = False,
        showarrow: bool = False,
        # showbackground: bool = False,
        showgrid: bool = None,
        showlabels: bool = False,
        showlegend: bool = None,
        # showline: bool = False,
        showscale: bool = False,
        showspikes: bool = False,
        showticklabels: bool = False,
        title: str = None,
        titlefont_size: int = 16,
        unlabeled: str = "Nodes",
        width: int = 1000,
        zeroline: bool = False
    ) -> go.Figure:
        """
        Returns Plotly figure from NetworkX graph.

        References for built-in color sequences:
        * [Built-in Colorscales](https://plotly.com/python/builtin-colorscales/)
        * [Colorscales](https://plotly.com/python/colorscales/)
        * [Templates](https://plotly.com/python/templates/)
        """
        pos = Plot._get_positions(G, pos)

        # Set default options if unset
        if showlabels and pos.shape[1] != 2:
            raise NotImplementedError("Showing labels only implemented for 2-dimensional plots.")

        if showgrid is None:
            showgrid = (showgrid is None and pos.shape[1] == 3)

        colorscale = colorscale if type(colorscale) == list else DEFAULT_COLOR_SEQUENCE\
                                if (colorscale in (True, None) and not groups) else None

        # Dictionary of node groups
        node_groups = {
            **{group: [] for group in (groups or {})},
            **({unlabeled: []} if sum([len(nodes) for nodes in (groups or {}).values()]) != G.order() else {})
        }
        list(node_groups[(groups or {}).get(node, unlabeled)].append(node) for node in G.nodes())

        # Size of nodes by degree
        min_node_size = 0

        if node_size is None:
            min_node_size = DEFAULT_SIZE
            node_size = pd\
                        .Series(dict(G.degree()))\
                        .dropna()\
                        .apply(lambda x: x + min_node_size)\
                        .to_dict()

        # Trace nodes per group
        node_traces = []

        for i, group, nodes in zip(range(len(node_groups)), node_groups.keys(), node_groups.values()):
            group_color = node_color if group == unlabeled else group_colors[::-1][-i-1]

            size = [
                node_size.get(node) if type(node_size) == dict else node_size
                for node in nodes
            ]

            color = [
                node_color.get(node) if type(node_color) == dict else (group_color or DEFAULT_NODE_COLOR)
                for node in nodes
            ]

            node_traces.append(
                (go.Scatter3d if pos.shape[1] == 3 else go.Scatter)(
                    x=pos["x"].values.tolist(),
                    y=pos["y"].values.tolist(),
                    mode="markers",
                    hoverinfo="text",
                    name=str(group).format(len(nodes)),
                    text=[labels.get(node, node) for node in nodes] if labels else nodes,
                    marker=dict(
                        color=[x - min_node_size for x in size] if colorscale else color,
                        colorscale=colorscale,
                        opacity=node_opacity,
                        reversescale=reversescale,
                        showscale=showscale,
                        size=size,
                        colorbar=dict(
                            title=colorbar_title,
                            thickness=colorbar_thickness,
                            titleside="bottom",
                            xanchor="left",
                        ),
                        line=dict(
                            color=node_line_color,
                            width=node_line_width,
                        )
                    ),
                    **(dict(z=pos["z"].values.tolist()) if pos.shape[1] == 3 else {})
                )
            )

        # Trace edges
        edge_trace = (go.Scatter3d if pos.shape[1] == 3 else go.Scatter)(
            x=[x for x in [(pos["x"][u], pos["x"][v]) for u, v in list(G.edges())] for x in x],
            y=[x for x in [(pos["y"][u], pos["y"][v]) for u, v in list(G.edges())] for x in x],
            mode="lines",
            hoverinfo="none",
            line=dict(
                color=edge_color or DEFAULT_EDGE_COLOR,
                width=edge_width,
            ),
            name="Edges",
            **(dict(z=[x for x in [(pos["z"][u], pos["z"][v]) for u, v in list(G.edges())] for x in x]) if pos.shape[1] == 3 else {})
        )

        axis = dict(
            showgrid=showgrid,
            showticklabels=showticklabels,
            zeroline=zeroline,
            showspikes=showspikes,
            title="",
        )

        fig = go.Figure(
            data=[edge_trace, *node_traces],
            layout=go.Layout(
                height=height,
                legend=dict(
                    y=0.5,
                    font=dict(
                        family=font_family,
                        size=font_size,
                        color=font_color,
                        ),
                    ),
                margin=dict(l=0, r=0, t=0, b=0),
                showlegend=showlegend if showlegend is not None else (True if len(node_traces) > 1 else False),
                title=title,
                titlefont=dict(
                    size=titlefont_size,
                ),
                width=width,
                xaxis=axis,
                yaxis=axis,
                scene=dict(
                    xaxis=axis,
                    yaxis=axis,
                    zaxis=axis,
                )
            ),
        )

        if showlabels:
            fig.update_layout(
                annotations=Plot._make_annotations(
                    labels=labels,
                    nodes=list(G.nodes()),
                    pos=pos,
                    showarrow=showarrow,
                )
            )

        return fig

    @staticmethod
    def histogram(
        G: nx.Graph,
        figsize: tuple = FIGSIZE,
        color: str = DEFAULT_NODE_COLOR,
        title: str = "Degree histogram"
    ) -> plt.Figure:
        """
        Returns histogram from NetworkX graph.
        """
        deg = sorted([d for n, d in G.degree()], reverse=True)
        degree_count = Counter(deg)
        deg, cnt = zip(*degree_count.items())
        fig, ax = plt.subplots(figsize=figsize)
        plt.bar(deg, cnt, width=0.80, color=color)
        # plt.title(title, fontsize=10, loc='center')
        plt.ylabel("Number of nodes", fontsize=12)
        plt.xlabel("Number of connections", fontsize=12)
        ax.set_xticks([d for d in deg])
        ax.set_xticklabels(d for d in deg) # fontsize=12
        ax.set_title(title)
        return fig

    @staticmethod
    def similarity_matrix(
        graphs: Union[dict, list],
        level: Literal["nodes", "edges"] = "nodes",
        output: str = None,
        figsize: tuple = (6,5),
        show: bool = False
    ) -> plt.Figure:
        """
        Returns node-level or edge-level similarity matrix from graphs.
        """
        keys = list(graphs.keys()) if type(graphs) == dict else range(len(graphs))

        indices = [
            Graph.nodes(graphs[i]).index
            if
                level == "nodes"
            else
                pd.Index(Graph
                         .edges(graphs[i]).iloc[:, [0, 1]]
                         .apply("->".join, axis=1))
            for i in keys
        ]

        df = pd.DataFrame({
            i: {
                j:
                    indices[i].shape[0]
                    if
                        i == j
                    else
                        indices[i]
                        .intersection(indices[j])
                        .shape[0]
                for j in keys

            }
            for i in keys
        })

        fig, ax = plt.subplots(figsize=figsize)

        sns.heatmap(
            df.divide(df.max(), axis=0).round(2),
            annot=True,
            ax=ax,
            center=.5,
            cmap="RdYlBu_r",
            linewidths=0,
        )

        if output:
            plt.savefig(output, bbox_inches="tight")
            df.astype(str).to_csv(f"{splitext(output)[0]}.csv", index=False)

        if show:
            plt.show()

        plt.close(fig)
        return fig

    @staticmethod
    def show(fig):
        plt.show(fig)

    @staticmethod
    def _make_annotations(
        pos: pd.DataFrame,
        color: str = "#555",
        labels: dict = None,
        nodes: list = None,
        offset: Union[int, float, dict] = 0,
        showarrow: bool = False,
        size: int = 12,
    ) -> list:
        """
        Adds node labels as text to Plotly 2-d figure.
        * [Example](https://plot.ly/~empet/14683/networks-with-plotly/)
        """
        return [
            dict(
                font=dict(
                    color=color,
                    size=size,
                ),
                showarrow=showarrow,
                text=labels.get(node) if labels else node,
                x=pos.loc[node][0],
                y=pos.loc[node][1] + (offset.get(node, 0) if type(offset) == dict else (offset or 0)),
                xref="x1",
                yref="y1",
                # xref="paper",
                # yref="paper",
                # xanchor="left",
                # yanchor="bottom",
            )
            for node in (nodes or pos.index)
        ]

    @staticmethod
    def _get_positions(
        G: nx.Graph,
        pos: Optional[Union[str, dict, pd.DataFrame]] = None
    ) -> pd.DataFrame:
        """
        Returns node positions as a DataFrame.
        """
        if pos is None or type(pos) == str:
            pos = Layout.layout(G, pos)

        if type(pos) == dict:
            pos = pd.DataFrame.from_dict(
                pos,
                orient="index",
            ).rename(
                columns={
                    0: "x",
                    1: "y",
                    2: "z"
                }
            )

        return pos.loc[list(G.nodes())]

    @staticmethod
    def _is_color(color: str) -> bool:
        """
        Returns True if string is a color.
        """
        try:
            plt.ColorConverter().to_rgb(color)
            return True
        except:
            return False

    plot = draw