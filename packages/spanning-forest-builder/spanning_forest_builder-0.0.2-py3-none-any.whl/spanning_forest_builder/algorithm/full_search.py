import numpy as np

def MST(nodes, edges):

    (tree, w) = iteration(nodes, edges, [])
    
    root = None
    if np.isinf(w) == False:
        root = find_roots(nodes, tree)[0]

    return (tree, w, root)


def iteration(nodes, edges, edges_merged):

    # Если выбранных дуг уже достаточно, то проверяем, что это дерево
    if len(edges_merged) == len(nodes) - 1:
        
        if is_tree(nodes, edges_merged):
            w = sum([e[2] for e in edges_merged])
            return (edges_merged, w)
        else:
            return ([], np.inf)

    # Иначе добавляем ещё дугу. Рекурсивно ищем минимальное дерево.
    else:
        w_min = np.inf
        tree_min = []

        for e in edges:
            
            (tree, w) = iteration(nodes, edges, edges_merged + [e])
            
            if w < w_min:
                w_min = w
                tree_min = tree

        return (tree_min, w_min)


def find_roots(nodes, edges):
    
    roots = []
    for n in nodes:
        inputs = 0
        for (u, v, w) in edges:
            if v == n:
                inputs += 1
        if inputs == 0:
            roots += [n]

    return roots


def is_tree(nodes, edges):

    # Ищем потенциальные корни
    r = find_roots(nodes, edges)

    # Корней больше 1
    if len(r) != 1:
        return False

    # Проверяем, что это дерево
    return is_tree_with_root(nodes, edges, r[0])


def is_tree_with_root(nodes, edges, root):

    # Проверяем, что дуг ровно len(nodes) - 1
    if len(edges) != len(nodes) - 1:
        return False
    
    # Проверяем, что все вершины достижимы из root.
    visited = []
    if go_down(nodes, edges, visited, root) == False:
        return False
    if len(visited) < len(nodes):
        return False
    
    return True


def go_down(nodes, edges, visited, u):

    visited += [u]
    
    for e in edges:
        if e[0] == u:
            if go_down(nodes, edges, visited, e[1]) == False:
                return False

    return True
