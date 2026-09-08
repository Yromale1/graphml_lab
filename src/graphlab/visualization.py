import networkx as nx
import matplotlib.pyplot as plt

CLASS_COLORS = {
    1: "red",
    2: "blue",
    3: "gray",
}

def view_graph(G: nx.Graph):

    pos = nx.spring_layout(G, seed=42)

    node_colors = [
        CLASS_COLORS.get(G.nodes[node].get("class"), "gray")
        for node in G.nodes
    ]

    nx.draw(
        G,
        pos,
        node_color=node_colors,
        node_size=30,
        arrows=True,
        with_labels=False,
    )

    plt.show()

def plot_neighborhood(G, node, radius=2, ax=None):

    if ax is None:
        _, ax = plt.subplots()

    nodes = nx.single_source_shortest_path_length(
        G.to_undirected(),
        node,
        cutoff=radius
    ).keys()

    subgraph = G.subgraph(nodes)

    pos = nx.spring_layout(subgraph, seed=42)

    node_colors = [
        CLASS_COLORS.get(subgraph.nodes[n].get("class"), "gray")
        for n in subgraph.nodes
    ]

    nx.draw(
        subgraph,
        pos,
        node_color=node_colors,
        node_size=100,
        arrows=True,
        alpha=0.7,
        with_labels=False,
        ax=ax,
    )

    ax.set_title(f"Neighborhood of {node}")

    return ax