import pandas as pd
import networkx as nx

def _create_graph(edges, df_features):
    G = nx.DiGraph()

    G.add_edges_from(
        edges[["txId1", "txId2"]].itertuples(
            index=False,
            name=None,
        )
    )
    class_map = df_features.set_index("txId")["class"].to_dict()

    nx.set_node_attributes(
        G,
        class_map,
        "class",
    )

    return G

def build_graph(path: str, path_features: str, path_classes: str) -> nx.Graph:
    """
    Build the graph from edge list.

    Parameters
    ----------
    path: str
        Path to the edge list dataset
    path_features: str
        Path to the node features dataset
    path_classes: str
        Path to the node classes dataset

    Returns
    -------
    G: nx.Graph
        The graph build from the edge
    """

    df = pd.read_csv(path)
    df_features = pd.read_csv(path_features)
    df_classes = pd.read_csv(path_classes)

    df_features = df_features[["txId", "Time step"]]
    df_features.insert(loc=2, column='class', value=df_classes['class'])

    valid_nodes = set(df_features["txId"])

    df = df[
        df["txId1"].isin(valid_nodes)
        & df["txId2"].isin(valid_nodes)
    ].copy()

    df = df.merge(
        df_features[['txId', 'Time step']],
        left_on='txId1',
        right_on='txId',
        how='left'
    )
    df = df.drop(columns=['txId'], errors='ignore')

    G = _create_graph(
        df,
        df_features,
    )

    return G

def build_graph_split(path: str, path_features: str, path_classes: str, t_val: int = 31, t_test: int = 36) -> nx.Graph:
    """
    Build the graph from edge list.

    Parameters
    ----------
    path: str
        Path to the edge list dataset
    path_features: str
        Path to the node features dataset
    path_classes: str
        Path to the node classes dataset
    t_val: int
        First time-step for the validation
    t_test: int
        First time_step for test

    Returns
    -------
    G_train: nx.Graph
        The training graph build from the edge
    G_val: nx.Graph
        The validation graph build from the edge
    G_test: nx.Graph
        The test graph build from the edge
    """

    df = pd.read_csv(path)
    df_features = pd.read_csv(path_features)
    df_classes = pd.read_csv(path_classes)

    df_features = df_features[["txId", "Time step"]]
    df_features.insert(loc=2, column='class', value=df_classes['class'])

    valid_nodes = set(df_features["txId"])

    df = df[
        df["txId1"].isin(valid_nodes)
        & df["txId2"].isin(valid_nodes)
    ].copy()

    df = df.merge(
        df_features[['txId', 'Time step']],
        left_on='txId1',
        right_on='txId',
        how='left'
    )
    df = df.drop(columns=['txId'], errors='ignore')


    G_train = _create_graph(
        df[df["Time step"] < t_val],
        df_features,
    )

    G_val = _create_graph(
        df[
            (df["Time step"] >= t_val)
            & (df["Time step"] < t_test)
        ],
        df_features,
    )

    G_test = _create_graph(
        df[df["Time step"] >= t_test],
        df_features,
    )

    return G_train, G_val, G_test