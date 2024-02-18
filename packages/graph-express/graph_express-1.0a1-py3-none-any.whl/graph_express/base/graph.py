from abc import ABCMeta
from os.path import isfile, splitext
from typing import Optional, Union

import igraph as ig
import logging as log
import networkit as nk
import networkx as nx
import pandas as pd
from networkx_gdf import GDF

from .convert import Convert

SUPPORT = ["gdf"]

READERS = sorted(SUPPORT + [method.replace('read_', '', 1)
                            for method in dir(nx.readwrite)
                            if method.startswith('read_')])

WRITERS = sorted(SUPPORT + [method.replace('write_', '', 1)
                            for method in dir(nx.readwrite)
                            if method.startswith('write_')])


class Graph(GDF, metaclass=ABCMeta):

    @staticmethod
    def adjacency(G: nx.Graph):
        """ Returns Pandas adjacency matrix from graph. """
        return nx.to_pandas_adjacency(G).astype(int, errors="ignore")

    @staticmethod
    def agg_edge_attr(G: nx.Graph, edge_attr: Optional[Union[str, list, bool]] = None) -> nx.Graph:
        """ Returns a NetworkX graph with aggregated edges/attributes. """
        groupby = ["source", "target"]

        if type(edge_attr) == str:
            groupby = [edge_attr]

        if type(edge_attr) == list:
            groupby += [column for column in edges.columns[2:] if column not in edge_attr]

        nodes = Graph.nodes(G, data=True)
        edges = Graph.edges(G, data=True)

        H = nx.convert_matrix\
              .from_pandas_edgelist(edges.groupby(groupby).agg(list).reset_index(),
                                    source="source",
                                    target="target",
                                    edge_attr=edge_attr,
                                    create_using=G)

        for attr in nodes.columns:
            nx.set_node_attributes(H, nodes[attr], attr)

        return H

    @staticmethod
    def agg_nodes(G: nx.Graph, node_attr: Union[str, dict, pd.Series, pd.DataFrame]) -> nx.Graph:
        """ Returns a NetworkX graph with grouped nodes by attribute. """
        if type(node_attr) == str:
            node_attr = Graph.nodes(G, node_attr)[node_attr]

        if type(node_attr) in (pd.Series, pd.DataFrame):
            node_attr = node_attr.squeeze().to_dict()

        H = Convert.pd2nx(
            [[node_attr[edge[0]], node_attr[edge[1]]] for edge in G.edges()],
            directed=G.is_directed(),
            multigraph=False,
            weighted=True,
        )

        return H

    @staticmethod
    def compose(list_of_graphs: list) -> nx.Graph:
        """ Returns a NetworkX graph composed from a list of graphs. """
        return nx.compose_all(list_of_graphs)

    @staticmethod
    def density(G: nx.Graph) -> float:
        """ Returns graph density, measure of its completeness. """
        return nx.density(G)

    @staticmethod
    def diameter(G: nx.Graph) -> float:
        """ Returns graph diameter, measure of its extension. """
        return nx.diameter(G)

    @staticmethod
    def edges(G: nx.Graph, data: Union[bool, str, list] = False, multi_index: bool = False) -> pd.DataFrame:
        """ Returns a Pandas data frame from edges in graph. """
        index = pd.MultiIndex.from_tuples(G.edges(data=False), names=["source", "target"])

        edges = pd.concat(
            [
                pd.DataFrame(
                    [x[2:] if type(data) == str else x[2] for x in G.edges(data=data)] if data else [],
                    columns=[data] if type(data) == str else None,
                    index=index,
                )
                for data in (data if type(data) == list else [data])
            ],
            axis=1
        )

        return edges if multi_index else edges.reset_index()

    @staticmethod
    def graph(directed: bool = False, multigraph: bool = False) -> nx.Graph:
        """ Returns empty NetworkX graph object. """
        if multigraph:
            return nx.MultiDiGraph() if directed else nx.MultiGraph()
        return nx.DiGraph() if directed else nx.Graph()

    @staticmethod
    def info(G: Union[nx.Graph, list, dict]) -> pd.Series or pd.DataFrame:
        """ Quickly describes graph(s) object(s). """
        if type(G) == list or type(G) == dict:
            index = list(G.keys() if type(G) == dict else range(len(G)))
            unique = len(set([_ for _ in [G[i].nodes() for i in index] for _ in _]))

            log.info(
                f"Total of {len(index)} graphs "
                f"with {sum(G[i].order() for i in index)} nodes ({unique} unique) "
                f"and {sum(G[i].size() for i in index)} edges.")

            return pd.DataFrame({"nodes": [G[i].order() for i in index],
                                "edges": [G[i].size() for i in index]},
                                index=index)

        log.info(
            f"{'Directed' if G.is_directed() else 'Undirected'} "
              f"{'multigraph' if G.is_multigraph() else 'graph'} "
              f"with {G.order()} nodes and {G.size()} edges.")

        return pd.Series({"nodes": G.order(), "edges": G.size()})

    @staticmethod
    def is_graph(object) -> bool:
        """ Returns True if object is a known graph instance. """
        return any(
            isinstance(object, graph)
            for graph in (nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph, nk.Graph, ig.Graph)
        )

    @staticmethod
    def isolates(G: nx.Graph) -> list:
        """ Returns list of node isolates. """
        return list(nx.isolates(G))

    @staticmethod
    def k_core(G: nx.Graph, k: int) -> nx.Graph:
        """ Returns k-cores after removing self-loops. """
        G.remove_edges_from(nx.selfloop_edges(G))
        return nx.k_core(G, k)

    @staticmethod
    def nodes(G: nx.Graph, data: Union[bool, str, list] = False) -> pd.DataFrame:
        """ Returns a Pandas data frame or series from nodes in graph. """
        return pd.concat(
            [
                pd.DataFrame(
                    [x[1:] if type(data) == str else x[1] for x in G.nodes(data=data)] if data else [],
                    columns=[data] if type(data) == str else None,
                    index=G.nodes(),
                )
                for data in (data if type(data) == list else [data])
            ],
            axis=1
        )

    @staticmethod
    def read_graph(path: str) -> nx.Graph:
        """ Returns a NetworkX graph object from file. """
        if type(path) is not str:
            raise TypeError(f"Expected 'str' type, got '{type(path).__name__}'.")

        if isfile(path):
            ext = splitext(path)[1].lower().lstrip(".")

            if ext == "gdf":
                try:
                    GDF.read_gdf(G, path)
                except:
                    raise RuntimeError(
                        "Please use the `read_gdf` method to import GDF files.")

            try:
                return getattr(nx, f"read_{ext}")(path)

            except AttributeError:
                raise AttributeError(
                    f"File extension not supported ('{ext}')."
                    f"Available formats: {READERS}.")

        raise FileNotFoundError(f"File '{path}' not found.")

    @staticmethod
    def remove_edges(G: nx.Graph, edges: list) -> nx.Graph:
        """ Remove node self-connections. """
        G.remove_edges_from(edges)
        return G

    @staticmethod
    def remove_nodes(G: nx.Graph, nodes: list) -> nx.Graph:
        """ Remove node self-connections. """
        G.remove_nodes_from(nodes)
        return G

    @staticmethod
    def remove_selfloop_edges(G: nx.Graph) -> nx.Graph:
        """ Remove node self-connections. """
        G.remove_edges_from(nx.selfloop_edges(G))
        return G

    @staticmethod
    def set_edge_attributes(G: nx.Graph, edge_attr: pd.DataFrame) -> nx.Graph:
        """ Returns NetworkX Graph object with edge attributes. """
        index = pd.MultiIndex.from_frame(Graph.edges(G, data=False))
        for attr in edge_attr:
            nx.set_edge_attributes(G, pd.Series(edge_attr[attr].values, index=index), attr)
        return G

    @staticmethod
    def set_node_attributes(G: nx.Graph, node_attr: pd.DataFrame) -> nx.Graph:
        """ Returns NetworkX Graph object with node attributes. """
        for attr in node_attr:
            nx.set_node_attributes(G, node_attr[attr], attr)
        return G

    @staticmethod
    def write_graph(G: nx.Graph, path: str) -> None:
        """ Writes a NetworkX graph object to file, if supported. """
        ext = splitext(path)[1].lower().lstrip(".")

        if ext == "gdf":
            GDF.write_gdf(G, path)

        else:
            try:
                getattr(nx, f"write_{ext}")(G, path)

            except AttributeError:
                raise AttributeError(
                    f"File extension not supported ('{ext}')."
                    f"Available formats: {WRITERS}.")
