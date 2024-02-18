import numpy as np
from .full_search import is_tree_with_root

def MST(nodes, edges):

    # Ищем минимум, перебирая все корни
    
    w_min = np.inf
    edges_merged_min = []
    root_min = None
    
    for root in nodes:
        
       (edges_merged, w, _) = MST_with_root(nodes, edges, root)

       if w < w_min:
            w_min = w
            edges_merged_min = edges_merged
            root_min = root

    return (edges_merged_min, w_min, root_min)


def MST_with_root(nodes, edges, root):
    
    edges_merged = iteration(nodes, edges.copy(), root)

    # Проверка, что это дерево
    if is_tree_with_root(nodes, edges_merged, root) == False:
        return ([], np.inf, None)

    w = sum(edge[2] for edge in edges_merged)

    return (edges_merged, w, root)


def iteration(nodes, edges, root):
    
    """
    Алгоритм Эдмондса.
    """

    """
    Шаг 1. Удаляем все дуги, идущие к корню.
    """
    
    for e in edges.copy():
        if e[1] == root:
            edges.remove(e)

    """
    Шаг 2. Для каждой вершины находим минимальную входящую дугу.
    """

    # словарь, сопоставляющий вершине минимальную входящую в неё дугу
    pi = dict()
    
    for e in edges:
        if ((pi.get(e[1]) is None) or (pi.get(e[1])[2] > e[2])):
            pi[e[1]] = e

    # набор минимальных дуг
    edges_min = set([pi[v] for v in pi.keys()])
    
    """
    Шаг 3. Находим циклы. Готовим новые данные для рекурсии. 
    """

    # есть ли циклы в графе
    cycled = False
    
    # уже перебранные вершины 
    nodes_used = set()
    
    # набор новых вершины (по несколько вершин старого графа сливаются в одну)
    nodes_new = set()
    
    # словарь, сопоставляющий старой вершине новую
    nodes_dict = dict()
    
    for v in nodes:
        if v in nodes_used:
            continue
        visited = set([v])
        e = pi.get(v)
        while True:
            # цикл оборвался
            if e is None:
                nodes_new.add(v)
                nodes_dict[v] = v
                nodes_used.add(v)
                break
            
            # вернулись обратно
            if e[0] == v:
                nodes_new.add(v)
                for u in visited:
                    nodes_dict[u] = v
                nodes_used.update(visited)
                cycled = True
                break

            # вернулись в посещённую вершину
            if e[0] in visited:
                nodes_new.add(v)
                nodes_dict[v] = v
                nodes_used.add(v)
                break

            visited.add(e[0])          
            e = pi.get(e[0])
    
    """
    Шаг 4. Если нет циклов, то мы построили дерево.
    """
    
    if cycled == False:
        return list(edges_min)
    
    """
    Шаг 5. Если циклы есть, то объединяем каждый цикл в вершину,
           пересчитываем дуги и рекурсивно вызываем алгоритм.
    """

    # словарь, сопоставляющий 2 новым вершинам новую дугу
    rho = dict()
    
    # словарь, сопоставляющий 2 новым вершинам старую дугу
    tau = dict()
    
    for e in edges:
        
        (u, v, w) = e
        
        u_new = nodes_dict[u]
        v_new = nodes_dict[v]
        index = (u_new, v_new)
        
        if u_new != v_new:
            
            # вес разрыва цикла
            """
            w_broke = 0
            e_broke = pi.get(v)
            if e_broke is not None:
                w_broke = [2]
            """
            w_broke = pi.get(v)[2]

            if ((rho.get(index) is None) or
                (rho.get(index)[2] > w - w_broke)):
                
                rho[index] = (u_new, v_new, w - w_broke)
                tau[index] = e

    edges_new = [rho[index] for index in rho.keys()]
    
    edges_new_merged = iteration(nodes_new, edges_new, nodes_dict[root])
    
    """
    Шаг 6. Разрываем циклы в нужных местах, получая дерево.
    """
    
    edges_merged = list(edges_min)
    for (u_new, v_new, w) in edges_new_merged:
        
        e = tau[(u_new, v_new)]
        if pi.get(e[1]) in edges_merged:
            edges_merged.remove(pi.get(e[1]))
        edges_merged += [e]

    return edges_merged
