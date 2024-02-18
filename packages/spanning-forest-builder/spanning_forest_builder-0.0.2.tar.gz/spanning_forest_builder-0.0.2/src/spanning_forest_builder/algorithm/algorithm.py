import numpy as np
from .Edmonds import MST_with_root


def MSF(nodes, edges, k):

    # Формируем начальные данные
    n = len(nodes)
    forest = [(set([node]), [], 0, node) for node in nodes]
    
    data = list()
    d_min = (None, None, None, np.inf)
    for e in edges:
        tree1 = (set([e[1]]), [], 0, e[1])
        tree2 = (set([e[0]]), [], 0, e[0])
        tree = (set([e[0], e[1]]), [e], e[2], e[0])
        d = (tree1, tree2, tree, e[2])
        data.append(d)
        if d[3] < d_min[3]:
            d_min = d    

    # Рекурсивно строим леса
    result = [get_edges(forest)]
    for i in range(n-k):
        if np.isinf(d_min[3]):
            # Невозможно построить лес с таким количеством деревьев!
            break
        (forest, data, d_min) = iteration(forest, edges, data, d_min)
        result = result + [get_edges(forest)]
    
    return result


def get_edges(forest):
    
    edges = []
    for tree in forest:
        edges += tree[1]
    return edges


def get_min_tree(tree1, tree2, edges_all):

    nodes = set()
    nodes.update(tree1[0])
    nodes.update(tree2[0])

    edges = list(filter(lambda e: ((e[0] in nodes) and (e[1] in nodes)),
                        edges_all))
    
    # Алгоритм Чу-Ли-Эдмондса
    (edges_merged, w, _) = MST_with_root(nodes, edges, tree1[3])
        
    tree = (nodes, edges_merged, w, tree1[3])
    return tree


def iteration(forest, edges_all, data, d_min):
    
    """
    forest = list( trees )
    tree = (set(some_nodes), list(some_edges), weight, root)
    
    edges_all = set( (u, v, w) )

    data = list( (tree1, tree2, tree, delta) )
    """

    data_new = list()
    d_min_new = (None, None, None, np.inf)

    (tree1, tree2, tree, delta) = d_min
    for d in data:
        if not ((d[0] == tree1) or (d[1] == tree1) or
                (d[0] == tree2) or (d[1] == tree2)):
            data_new.append(d)
            if d[3] < d_min_new[3]:
                d_min_new = d
              
    forest.remove(tree1)
    forest.remove(tree2)
    
    for t in forest:
        t_new1 = get_min_tree(tree, t, edges_all)
        t_new2 = get_min_tree(t, tree, edges_all)
        delta1 = t_new1[2] - t[2] - tree[2]
        delta2 = t_new2[2] - t[2] - tree[2]
        d1 = (tree, t, t_new1, delta1)
        d2 = (t, tree, t_new2, delta2)
        data_new.append(d1)
        data_new.append(d2)
        if d1[3] < d_min_new[3]:
            d_min_new = d1
        if d2[3] < d_min_new[3]:
            d_min_new = d2
    
    forest.append(tree)

    return (forest, data_new, d_min_new)
