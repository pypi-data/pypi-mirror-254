from abc import ABCMeta
from typing import Optional, Union

import igraph as ig
import networkx as nx
import networkit as nk
import pandas as pd

try:
    from torch_geometric.data import data as pyg_data
    from torch_geometric.utils import to_networkx as pyg_to_networkx
    from torch_geometric.utils.convert import from_networkx as pyg_from_networkx
except ImportError:
    pyg_data = None
    pyg_from_networkx = lambda x: None
    pyg_to_networkx = lambda x, to_undirected: None


class Convert(metaclass=ABCMeta):

    @staticmethod
    def ig2nk(iG: ig.Graph) -> nk.Graph:
        """ Returns igraph graph as NetworkX object. """
        return Convert.nx2nk(iG.to_networkx())

    @staticmethod
    def ig2nx(iG: ig.Graph) -> nx.Graph:
        """ Returns igraph graph as NetworkX object. """
        return iG.to_networkx()

    @staticmethod
    def nk2ig(nkG: nk.Graph, index=[]) -> ig.Graph:
        """ Returns Networkit graph as igraph object. """
        iG = ig.Graph(directed=nkG.isDirected())
        iG.add_vertices(list(nkG.iterNodes()) if not index else index)
        iG.add_edges(list(nkG.iterEdges()))
        iG.es["weight"] = list(nkG.iterEdgesWeights())
        return iG

    @staticmethod
    def nk2nx(nkG: nk.Graph, index={}) -> nx.Graph:
        """ Returns Networkit graph as NetworkX object. """
        G = nk.nxadapter.nk2nx(nkG)
        if index:
            G = nx.relabel.relabel_nodes(G, index)
        return G

    @staticmethod
    def nx2ig(G: nx.Graph) -> ig.Graph:
        """ Returns NetworkX graph as igraph object. """
        iG = ig.Graph.from_networkx(G)
        # edgelist = nx.to_pandas_edgelist(G)
        # for attr in edgelist.columns[2:]:
        #     iG.es[attr] = edgelist[attr]
        return iG

    @staticmethod
    def nx2nk(G: nx.Graph) -> nk.Graph:
        """ Returns NetworkX graph as Networkit object. """
        return nk.nxadapter.nx2nk(G) if G.order() > 0 else nk.Graph()

    @staticmethod
    def nx2pyg(G: nx.Graph) -> pyg_data:
        """ Returns PyTorch Geomtric data from NetworkX graph. """
        return pyg_from_networkx(G)

    @staticmethod
    def pd2nx(
        edges: Optional[Union[list, pd.DataFrame]] = None,
        nodes: Optional[Union[list, pd.DataFrame]] = None,
        source: Optional[str] = None,
        target: Optional[str] = None,
        directed: Optional[bool] = False,
        multigraph: Optional[bool] = None,
        weighted: Optional[bool] = None,
        edge_attr: Optional[Union[list, bool]] = True,
        node_attr: Optional[Union[list, bool]] = True,
        edge_key: Optional[str] = None,
        node_key: Optional[str] = None,
        isolates: Optional[bool] = False,
        selfloops: Optional[bool] = False,
        create_using: Optional[Union[nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph]] = None,
    ) -> nx.Graph:
        """ Returns NetworkX graph object from lists or Pandas data frames. Aliases: `graph`, `pd2nx`. """
        if nodes is None:
            nodes = pd.DataFrame()
        elif type(nodes) == list:
            nodes = pd.DataFrame(nodes)

        if edges is None:
            edges = pd.DataFrame(columns=[source or "source", target or "target"])
        elif type(edges) == list:
            edges = pd.DataFrame(edges, columns=[source or "source", target or "target"])


        if not (source and target):
            if all(_ in edges.columns.tolist() for _ in ["source", "target"]):
                source, target = "source", "target"
            elif edges.shape[1] == 2:
                source, target = edges.columns.tolist()

        if any(_ not in edges.columns for _ in (source, target)):
            raise RuntimeError("Missing 'source' and/or 'target' attributes. "
                               f"Received: {[source, target]}, available: {edges.columns.tolist()}.")

        # Allow multiple edges among nodes if found.
        if multigraph is None and edges[[source, target]].duplicated().any():
            multigraph = True

        # Object type to build graph with.
        if create_using is None:
            create_using = nx.DiGraph() if directed else nx.Graph()
            if multigraph:
                create_using = nx.MultiDiGraph() if directed else nx.MultiGraph()

        # Edge attributes to consider.
        if edge_attr is True:
            edge_attr = [_ for _ in edges.columns if _ not in (source, target)]

        # Node attributes to consider.
        if node_attr is True:
            node_attr = [_ for _ in nodes.columns if _ != node_key]

        # Convert edge list to graph.
        G = nx.convert_matrix\
              .from_pandas_edgelist(edges,
                                    source=source,
                                    target=target,
                                    edge_attr=edge_attr or None,
                                    edge_key=edge_key or None,
                                    create_using=create_using)

        # Assign weights to edges...
        if not multigraph and weighted is not False:
            weight = pd.DataFrame({"source": edges[source],
                                   "target": edges[target],
                                   "weight": edges["weight"] if "weight" in edges.columns else 1})\
                        .groupby([source, target])\
                        .sum("weight")\
                        .squeeze("columns")
            # ...if 'weighted' is True or edge weights are not all one.
            if weighted is True or not weight.min() == 1 == weight.max():
                nx.set_edge_attributes(G, weight, "weight")

        # Add disconnected nodes to graph.
        if isolates is True:
            G.add_nodes_from(nodes.index if node_key is None else nodes[node_key])

        # Remove self-connections from graph.
        if selfloops is False:
            G.remove_edges_from(nx.selfloop_edges(G))

        # Assign attributes to nodes.
        for attr in (node_attr or []):
            nx.set_node_attributes(G,
                                   nodes[attr] if node_key is None
                                               else pd.Series(nodes[attr].values,
                                                              index=nodes[node_key].values),
                                   attr)

        return G

    @staticmethod
    def pyg2nx(data: pyg_data, to_undirected: bool = False) -> nx.Graph:
        """ Returns NetworkX graph from PyTorch Geometric data. """
        return pyg_to_networkx(data, to_undirected=to_undirected) # data._data
