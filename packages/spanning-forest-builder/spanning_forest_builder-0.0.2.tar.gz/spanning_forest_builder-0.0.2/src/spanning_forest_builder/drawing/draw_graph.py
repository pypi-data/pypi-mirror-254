import networkx as nx
import matplotlib.pyplot as plt
import os
from . import draw_edge_labels as dl


def save_forests(nodes, forests,
                 folder_path="images"):
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            pass
        
    i = 0
    for forest in forests:
        path = folder_path + "\\" + str(i)
        title = "Лес из " + str(len(nodes) - i) + " деревьев"
        save_graph(nodes, forest, title="", path=path)
        i += 1
        

def save_graph(nodes, edges, title="", path="graph"):

    path += ".png"
    folder_path, _ = os.path.split(path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    fig = draw_graph(nodes, edges, title="")
    fig.savefig(path)
    plt.close(fig)


def draw_graph(nodes, edges, title=""):

    G = nx.DiGraph(directed=True)
    G.add_nodes_from(nodes)
    G.add_edges_from(list_to_dict(edges))

    return draw_nx_graph(G, title)


def draw_nx_graph(G, title=""):

    fig, ax = plt.subplots()
    plt.title(title)

    # set layout
    pos = nx.circular_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)

    curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
    straight_edges = list(set(G.edges()) - set(curved_edges))
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges)
    arc_rad = 0.2
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges,
                       connectionstyle=f'arc3, rad = {arc_rad}')

    # draw edge labels
    edge_weights = nx.get_edge_attributes(G, 'w')
    curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
    straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
    dl.draw_labels(
        G,
        pos,
        ax = ax,
        edge_labels = curved_edge_labels,
        bbox = dict(boxstyle='round', facecolor='wheat', alpha=0.85),
        rotate = False,
        rad = arc_rad)
    dl.draw_labels(
        G,
        pos,
        ax = ax,
        edge_labels = straight_edge_labels,
        bbox = dict(boxstyle='round', facecolor='wheat', alpha=0.85),
        rotate = False)

    fig.canvas.draw()

    return fig


def list_to_dict(l):
    d = []
    for e in l:
        x = (e[0], e[1], {'w':e[2]})
        d.append(x)
    return d
