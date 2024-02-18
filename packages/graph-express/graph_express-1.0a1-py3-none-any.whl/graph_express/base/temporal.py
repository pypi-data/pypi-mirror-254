from abc import ABCMeta
from typing import Any, Callable, Literal, Optional, Union

import logging as log
import networkx as nx
import pandas as pd

from .graph import Graph


class Temporal(metaclass=ABCMeta):

    @staticmethod
    def snapshot_temporal_graph(
        G: nx.Graph,
        attr: Union[str, list, dict],
        attr_level: Literal["node", "edge"],
        cut_level: Literal["node", "edge"] = "edge",
        node_level: Literal["source", "target"] = "source",
        steps: Optional[int] = None,
        qcut: bool = False,
        duplicates: bool = True,
        rank_first: bool = False,
        factorize: bool = True,
        apply_func: Optional[Callable[..., Any]] = None,
        fillna: Optional[Any] = None
    ) -> dict:
        """
        Returns snapshot-based temporal graph (STG), a dictionary of graphs where
        each key is a time step and each value is a subgraph of the original graph.

        - `attr`:
            Attribute key to consider for snapshots, in case of a string.
            Also accepts a list or a dictionary as input, which must have
            the same length as the number of nodes or edges in the graph,
            depending on the selected `attr_level` argument parameter.
        - `attr_level`:
            Whether the given `attr` is a property of "node" or "edge".
        - `cut_level`:
            Whether to balance "edge" (default) or "node" number among snapshots.
        - `node_level`:
            Whether time attribute refers to "source" (default) or "target" node.
            Only used if `attr_level` or `cut_level` are set as "node".
        - `steps`:
            Number of snapshots to return. Must be greater than or equal to 1.
        - `qcut`:
            If `True`, balances snapshot based on quantiles.
        - `duplicates`:
            If `False`, allows Pandas to ignore duplicate points generating snapshots.
        - `rank_first`:
            If `True`, considers each data point as unique when generating snapshots.
        - `factorize`:
            If `True`, returns integer-based dictionary keys: [0, 1, 2, ...].
            Default is `True` if any number of `steps` (>1) is given.
        - `apply_func`:
            Function to apply on node-level or edge-level data to obtain time steps.
        """
        attr_level = attr_level.rstrip("s") if type(attr_level) == str else attr_level
        cut_level = cut_level.rstrip("s") if type(cut_level) == str else cut_level

        assert type(attr) != str or attr_level in ("node", "edge"),\
            "Argument `attr_level` must be either 'node' or 'edge'."

        assert cut_level in ("node", "edge"),\
            "Argument `cut_level` must be either 'node' or 'edge'."

        assert node_level in ("source", "target"),\
            "Argument `node_level` must be either 'source' or 'target'."

        log.info(f"Original graph: |V|={G.order()}, |E|={G.size()}")

        # Obtain temporal data from node-level or edge-level attribute.
        times = pd.Series(
            attr.squeeze()
                if type(attr) == pd.DataFrame else
                getattr(Graph, f"{attr_level}s")(G, attr).squeeze()
                if type(attr) == str else attr,
            **(dict(index=G.nodes()) if type(attr) == list and attr_level == "node" else {})
        )

        assert attr_level == "edge" or len(times) == G.order(),\
            f"Length of `attr` differs from number of nodes ({len(times)}, {G.order()})."

        assert attr_level == "node" or len(times) == G.size(),\
            f"Length of `attr` differs from number of edges ({len(times)}, {G.size()})."

        if times.isna().any():
            assert not times.isna().all(),\
                f"Attribute does not exist or contains null values only."
            assert fillna is not None,\
                f"Found null value(s) in attribute data, but `fillna` has not been set."
            times.fillna(fillna, inplace=True)

        edges = Graph.edges(G, data=False)

        # Apply function to time attribute values.
        if apply_func is not None:
            times = times.apply(apply_func)

        # Obtain edge temporal values from node-level data [0/1].
        if attr_level == "node":
            times = edges[node_level].apply(times.get)

        # Return a given number of time steps.
        if steps:

            # Obtain node-wise (source or target) cut to consider for time steps.
            if cut_level == "node":
                times = [
                    pd.Series(
                        times.loc[nodes.index].values,
                        index=nodes.values
                    )
                    for nodes in
                        [edges[node_level].drop_duplicates().sort_values()]
                ][0]

            # Treat data points sequentially.
            if rank_first:
                times = times.rank(method="first")

            # Cut data in a given nuber of time steps.
            times = getattr(pd, "qcut" if qcut else "cut")(
                times,
                steps,
                duplicates="drop" if duplicates is False else "raise"
            )

            log.info(f"Generated {'qcut' if qcut else 'cut'} "
                     f"(t={times.unique().shape[0]}) "
                     f"considering {times.shape[0]} data points.")

            # Obtain edge temporal values from node-level data [1/1].
            if cut_level == "node":
                times = edges[node_level].apply(times.get)

        # Return integer-based keys.
        if factorize:
            times = pd.Series(
                pd.factorize(times, sort=True)[0],
                index=times.index
            )

        STG = {t.__str__() if steps and not factorize else t:
               G.edge_subgraph(edges.loc[index].apply(tuple, axis=1))
               for t, index in edges.groupby(times).groups.items()}

        list(log.info(f"Snapshot {t}: |V|={S.order()}, |E|={S.size()}")
             for t, S in STG.items())

        return STG

    @staticmethod
    def event_temporal_graph(G: nx.Graph) -> list:
        """
        Returns event-based temporal graph (ETG) list.

        While the snapshot-based temporal graph (STG) is a dictionary of graphs, where
        each key is a time step and each value is a subgraph of the original graph, the
        event-based temporal graph (ETG) is a list of events, e.g., (u, v, t), where
        u and v are nodes and t is the time step when the edge (u, v) was created.
        """
        raise NotImplementedError("Method not implemented yet.")

    @staticmethod
    def unified_temporal_graph(
        STG: Union[list, dict],
        add_couplings: bool = True,
        add_index: bool = False,
        add_proxy_nodes: bool = False,
        proxy_nodes_with_attr: bool = True,
        prune_proxy_nodes: bool = True,
        node_index: list = None,
    ) -> nx.Graph:
        """
        Returns unified temporal graph (UTG) from snapshot temporal graph (STG).

        The UTG is a single graph that contains all the nodes and edges of an STG,
        plus proxy nodes and edge couplings connecting sequential temporal nodes.
        """
        T = list(STG.keys() if type(STG) == dict else range(len(STG)))

        # Build empty graph of the same type.
        UTG = Graph.graph(directed=STG[T[0]].is_directed(),
                          multigraph=STG[T[0]].is_multigraph())

        assert all(STG[t].is_directed() == UTG.is_directed() for t in T),\
               "Mixed graphs and digraphs are not supported."

        assert all(STG[t].is_multigraph() == UTG.is_multigraph() for t in T),\
               "Mixed graphs and multigraphs are not supported."

        # Add intra-slice nodes and edges,
        # relabeling nodes to include temporal index.
        UTG = nx.compose_all([
            nx.relabel_nodes(
                STG[t],
                {v: f"{v}_{t}" for v in STG[t].nodes()}
            )
            for t in T
        ])

        # Add proxy nodes on sebsequent slices.
        if add_proxy_nodes:
            proxy_nodes = Temporal._proxy_nodes(STG, prune_proxy_nodes)
            # Compose attributed graph containing node isolates only.
            if proxy_nodes_with_attr:
                G = nx.compose_all(
                    nx.create_empty_copy(
                        STG[t].subgraph(nodes)
                    )
                    for t, nodes in {
                        t: [
                            node
                            for node, interval in proxy_nodes.items()
                            if interval[0] == t
                        ]
                        for t in T
                    }
                    .items()
                )
            # Include proxy nodes in unified temporal graph.
            list(
                (
                    UTG := nx.compose(
                        UTG,
                        nx.relabel_nodes(
                            G.subgraph(nodes),
                            {v: f"{v}_{t}" for v in nodes}
                        )
                    )
                )
                if proxy_nodes_with_attr else
                    UTG.add_nodes_from(
                        [f"{v}_{t}" for v in nodes]
                    )
                for t, nodes in {
                    t: [
                        node
                        for node, interval in proxy_nodes.items()
                        if t in range(interval[0]+1, interval[1]+1)
                        and not STG[t].has_node(node)
                    ]
                    for t in T
                }
                .items()
            )

        # Add inter-slice couplings among temporal nodes.
        if add_couplings:
            UTG.add_edges_from(
                Temporal._couplings(
                    STG,
                    proxy_nodes if add_proxy_nodes else None
                )
            )

        # Add original node index and temporal index as attributes.
        if add_index:
            nx.set_node_attributes(
                UTG,
                {
                    node: {
                        "t": node.rsplit("_", 1)[1],
                        "v": node_index.index(int(node.rsplit("_", 1)[0])) if node_index else node.rsplit("_", 1)[0],
                    }
                    for node in UTG.nodes()
                }
            )

        return UTG

    @staticmethod
    def flatten_temporal_graph(TG: Union[dict, list]):
        """
        Returns flattened graph from a temporal graph.

        A flattened graph is a single graph containing all nodes
        and edges of a temporal graph (snapshot-based or event-based).
        """
        return nx.compose_all(TG.values() if type(TG) == dict else TG)

    @staticmethod
    def _couplings(STG: Union[dict, list], proxy_nodes: Optional[dict] = None):
        T = list(STG.keys() if type(STG) == dict else range(len(STG)))

        couplings = set()
        for i in range(len(T)-1):
            for node in STG[T[i]].nodes():
                for j in range(i+1, len(T)):
                    if STG[T[j]].has_node(node)\
                    or ((proxy_nodes or {}).get(node) and j-1 in range(*proxy_nodes.get(node))):
                        couplings.add((f"{node}_{T[i]}", f"{node}_{T[j]}"))
                        break

        if proxy_nodes:
            list(
                couplings.add((f"{node}_{T[t-1]}", f"{node}_{T[t]}"))
                for node, bounds in proxy_nodes.items()
                for t in range(bounds[0]+1, bounds[1]+1)
            )

        return couplings

    @staticmethod
    def _proxy_nodes(STG: Union[dict, list], prune: bool = False):
        T = list(STG.keys() if type(STG) == dict else range(len(STG)))

        proxy_nodes = {}
        for i in range(len(T)-1):
            for node in STG[T[i]].nodes():
                if not proxy_nodes.get(node):
                    for j in reversed(range(min(i+2, len(T)), len(T))):
                        if STG[T[j]].has_node(node) or not prune:
                            proxy_nodes[node] = (i, j)
                            break

        return proxy_nodes
