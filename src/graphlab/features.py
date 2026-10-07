import networkx as nx
import pandas as pd


def compute_degree(G: nx.DiGraph, df: pd.DataFrame):

    in_degree = pd.Series(dict(G.in_degree()))
    out_degree = pd.Series(dict(G.out_degree()))

    df['in_degree'] = df['txId'].map(in_degree)
    df['out_degree'] = df['txId'].map(out_degree)
    df["total_degree"] = (
        df["in_degree"] +
        df["out_degree"]
    )
    return df

def compute_pagerank(G: nx.DiGraph, df: pd.DataFrame):

    pagerank = nx.pagerank(G)

    df["pagerank"] = df["txId"].map(pagerank)

    return df

def compute_clustering(G: nx.DiGraph, df: pd.DataFrame):

    clustering = nx.clustering(G)

    df['clustering'] = df['txId'].map(clustering)

    return df

def neighborhood_size(G, node, distance):
    lengths = nx.single_source_shortest_path_length(
        G,
        node,
        cutoff=distance
    )
    return sum(1 for d in lengths.values() if d == distance)

def compute_neighborhood(G: nx.DiGraph, df: pd.DataFrame):

    df["neighbors_1hop"] = df["txId"].map(
        lambda x: len(set(G.predecessors(x)) | set(G.successors(x)))
    )
    
    G_undirected = G.to_undirected()

    df["neighbors_2hop"] = df["txId"].map(
        lambda x: neighborhood_size(G_undirected, x, 2)
    )

    return df

def compute_centrality(G: nx.DiGraph, df: pd.DataFrame):

    betweenness = nx.betweenness_centrality(G)

    df['betweenness'] = df['txId'].map(betweenness)

    closeness = nx.closeness_centrality(G)

    df['closeness'] = df['txId'].map(closeness)

    return df