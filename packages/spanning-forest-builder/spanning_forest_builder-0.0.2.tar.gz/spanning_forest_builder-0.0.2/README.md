Библиотека для построения ориентированных лесов минимального веса.

**Алгоритм основан на статьях:**\
[springer.com](https://link.springer.com/article/10.1007/s10958-023-06666-w)\
[Записки научных семинаров ПОМИ](http://ftp.pdmi.ras.ru/pub/publicat/znsl/v497/p005.pdf)

# Описание алгоритма

Пусть изначально имеется граф *G* с *N* вершинами.

**Старт**\
Все вершины без дуг (нулевой граф) - лес из *N* деревьев.

**Шаг 1**\
Ищем среди всех дуг дугу с минимальным весом.\
Лес из *N-1* деревьев будет содержать только эту дугу.

...

**Шаг *i***\
На предыдущем шаге построен лес *F* из *N-i+1* деревьев.\
Для каждой пары различных деревьев *T_j*, *T_k* из *F* найдём (с помощью алгоритма Эдмондса)
дерево минимального веса *T_jk* (только из вершин*T_j*, *T_k* и с корнем в корне *T_j*) и его вес *w_jk*. 
Для каждой тако пары вычислим добавку к весу леса, которая получится, если мы соединим *T_j* и *T_k*, 
по формуле *d_jk = w_jk - w_j - w_k*.\
Найдём минимум *d_jk* по индексам *j*, *k*. Пусть он достигается при *j = m*, *k = n*.\
В качестве леса из *N-i* деревьев возьмём *T_mn* и все *T_j*, где *j ≠ m, n*.

**Замечание 1.** Алгоритм можно остановить на любом шаге, получив лес из *N-i* деревьев.\
**Замечание 2.** Если дойти до *N*-го шага, то мы получим дерево минимального веса (лес из 1 дерева).\
**Замечание 3.** Если исходный граф был неполным, то алгоритм может остановиться раньше, 
чем дойдёт до *N*-го шага (например, на *i*-ом шаге). Это означает, что *i* - минимальное количество
деревьев в лесу из графа *G*.\
**Замечание 4.** На каждом шаге достаточно пересчитывать *T_jk* только с деревом, полученным 
на предыдущем шаге. Остальные останутся такими же.

# Функции

 -  Лес минимального веса из *k* деревьев (*N-k* шагов алгоритма)
	```Python
	forests = algorithm.MSF(nodes, edges, k)
	```
	 - *nodes* - массив вершин. Название вершины может быть любым неизменяемым типом данных 
		(например, число или строка).
	 - *edges* - массив дуг в формате (вершина1, вершина2, вес). Вес может быть не целым и отрицательным.
	 - *k* - число от 1 до *N* включительно.
	 - *forests* - массив из *N-k+1* элементов (если алгоритм оборвётся раньше, то элементов будет меньше).
		*i*-ый элемент массива - набор дуг леса из *N-i* деревьев. Массив будет выглядеть так: \
	    forests[0] = [] (нет дуг)\
		forests[1] = [(u, v, w)] (одна дуга из вершины *u* в вершину *v* с весом *w*)\
		...
	 
 -  Дерево минимального веса с заданным корнем (алгоритм Эдмондса)
	```Python
	tree, w, root = Edmonds.MST_with_root(nodes, edgesб root)
	```
	 - *nodes* - массив вершин. Название вершины может быть любым неизменяемым типом данных 
		(например, число или строка).
	 - *edges* - массив дуг в формате (вершина1, вершина2, вес). Вес может быть не целым и отрицательным.
	 - *root* - корень полученного дерева (из массива *nodes*)
	 - *tree* - набор дуг дерева. Набор будет выглядеть так: \
	    tree = [(u1, v1, w1), (u2, v2, w2), ...]
	 - *w* - вес полученного дерева (число)\
	Если дерево построить невозможно, возвращает ([], np.inf, None).

 -  Дерево минимального веса (алгоритм Эдмондса с перебором корней)
	```Python
	tree, w, root = Edmonds.MST(nodes, edges)
	```
	 - *nodes* - массив вершин. Название вершины может быть любым неизменяемым типом данных 
		(например, число или строка).
	 - *edges* - массив дуг в формате (вершина1, вершина2, вес). Вес может быть не целым и отрицательным.
	 - *tree* - набор дуг дерева. Набор будет выглядеть так: 
	    tree = [(u1, v1, w1), (u2, v2, w2), ...]\
	 - *w* - вес полученного дерева (число)
	 - *root* - корень полученного дерева (из массива *nodes*)\
	Если дерево построить невозможно, возвращает ([], np.inf, None).
	
 -  Дерево минимального веса (полный перебор дуг)
	```Python
	tree, w, root = full_search.MST(nodes, edges)
	```
	 - *nodes* - массив вершин. Название вершины может быть любым неизменяемым типом данных 
		(например, число или строка).
	 - *edges* - массив дуг в формате (вершина1, вершина2, вес). Вес может быть не целым и отрицательным.
	 - *tree* - набор дуг дерева. Набор будет выглядеть так: \
	    tree = [(u1, v1, w1), (u2, v2, w2), ...]
	 - *w* - вес полученного дерева (число)
	 - *root* - корень полученного дерева (из массива *nodes*)\
	Если дерево построить невозможно, возвращает ([], np.inf, None).

 -  Проверка того, что набор дуг образует дерево
	```Python
	a = full_search.is_tree(nodes, edges)
	```
	 - *nodes* - массив вершин. Название вершины может быть любым неизменяемым типом данных 
		(например, число или строка).
	 - *edges* - массив дуг в формате (вершина1, вершина2, вес). Вес может быть не целым и отрицательным.
	 - *a* - равно *True*, если *edges* образуют дерево.
	 
 -  Проверка того, что набор дуг образует дерево с заданным корнем
	```Python
	a = full_search.is_tree_with_root(nodes, edges, root)
	```
	 - *nodes* - массив вершин. Название вершины может быть любым неизменяемым типом данных 
		(например, число или строка).
	 - *edges* - массив дуг в формате (вершина1, вершина2, вес). Вес может быть не целым и отрицательным.
	 - *root* - корень полученного дерева (из массива *nodes*)
	 - *a* - равно *True*, если *edges* образуют дерево.
	 
 -  Нарисовать граф
	```Python
	fig = draw_graph(nodes, edges, title="")
	```
	 - *nodes* - массив вершин. Название вершины может быть любым неизменяемым типом данных 
		(например, число или строка).
	 - *edges* - массив дуг в формате (вершина1, вершина2, вес). Вес может быть не целым и отрицательным.
	 - *title* - заголовок Фигуры.
	 - *fig* - фигура из *matplotlib*.
	 
 -  Сохранить граф как рисунок
	```Python
	save_graph(nodes, edges, title="", path="graph")
	```
	 - *nodes* - массив вершин. Название вершины может быть любым неизменяемым типом данных 
		(например, число или строка).
	 - *edges* - массив дуг в формате (вершина1, вершина2, вес). Вес может быть не целым и отрицательным.
	 - *title* - заголовок Фигуры.
	 - *path* - путь сохранения. Например, если *path="images//graph1"*, то граф будет сохранён 
		в директорию *images* в файл *graph1.png*.

 -  Сохранить набор лесов как рисунки
	```Python
	save_forests(nodes, forests, folder_path="images")
	```
	 - *nodes* - массив вершин. Название вершины может быть любым неизменяемым типом данных 
		(например, число или строка).
	 - *forests* - массив лесов.
	 - *folder_path* - путь сохранения.

# Примеры

## Пример 1. Основные функции
```Python
# Импортируем библиотеки
from spanning_forest_builder import *
import matplotlib.pyplot as plt

# Создаем массивы вершин и дуг
# Массив дуг состоит из кортежей (вершина1, вершина2, вес)
n = 6
nodes = list(range(n))
edges = [(0, 1, 3),
         (0, 5, 10),
         (1, 2, 4),
         (3, 1, 2),
         (3, 4, 3),
         (4, 1, 10),
         (4, 3, 1),
         (5, 0, 6),
         (5, 1, 10),
         (5, 4, 7)]

# Строим леса и деревья
forests = algorithm.MSF(nodes, edges, 1)
tree1, _, _ = Edmonds.MST(nodes, edges)
tree2, _, _ = Edmonds.MST_with_root(nodes, edges, 0)
tree3, _, _ = full_search.MST(nodes, edges)

# Рисуем исходный граф
draw_graph(nodes, edges, title="Исходный граф")

# Рисуем лес из 4 деревьев
draw_graph(nodes, forests[2], title="Лес из 4 деревьев")

# Сохраняем леса в папку images//forests
save_forests(nodes, forests, folder_path="images//forests")

# Сохраняем деревья в папку images
save_graph(nodes, tree1,
           title="Edmonds",
           path="images//Edmonds")
save_graph(nodes, tree2,
           title="Edmonds with root 0",
           path="images//Edmonds with root 0")
save_graph(nodes, tree3,
           title="full_search",
           path="images//full_search")

# Показывае нарисованные графы
plt.show()
```

## Пример 2. Время работы
```Python
from spanning_forest_builder import *
import random, time
import matplotlib.pyplot as plt

def generate(n):
    edges = []
    for i in range(n):
        for j in range(n):
            w = random.randint(-10, 10)
            if (j != i) and (w > 0):
                edges += [(i, j, w)]
    return edges

samples = 100
n = 30
nodes = list(range(n))

no_builded = 0
errors = 0
time1 = 0
time2 = 0

for i in range(samples):
    
    edges = generate(n)

    t0 = time.perf_counter_ns()
    res1 = Edmonds.MST(nodes, edges)[0]
    t1 = time.perf_counter_ns()
    res2 = algorithm.MSF(nodes, edges, 1)[-1]
    t2 = time.perf_counter_ns()
    
    w1 = sum(e[2] for e in res1)
    w2 = sum(e[2] for e in res2)

    if len(res1) == 0:
        no_builded += 1
        continue

    if (len(res1) != len(res2)) or (len(res1) != n-1):
        errors += 1
        
    if w1 != w2:
        errors += 1

    if w1 == w2:
        time1 += t1-t0
        time2 += t2-t1


print("Ошибок:", errors)
print("Невозможно построить дерево:", no_builded)
print("Среднее время алгоритма Эдмондса (наносекунд):", time1 / (samples - no_builded))
print("Среднее время алгоритма MSF      (наносекунд):", time2 / (samples - no_builded))
```

## Пример 3. Время работы
```Python
from spanning_forest_builder import *
import random, time, math
import matplotlib.pyplot as plt

def generate(n):
    edges = []
    for i in range(n):
        for j in range(n):
            w = random.randint(-90, 10)
            if (j != i) and (w > 0):
                edges += [(i, j, w)]
    return edges


no_builded = 0
errors = 0

x = []
f1 = []
f2 = []
n_min = 10
n_max = 100
N = range(n_min, n_max)

for n in N:
    print(n)

    nodes = list(range(n))
    edges = generate(n)

    t0 = time.perf_counter_ns()
    res1 = Edmonds.MST(nodes, edges)[0]
    t1 = time.perf_counter_ns()
    res2 = algorithm.MSF(nodes, edges, 1)[-1]
    t2 = time.perf_counter_ns()
    
    w1 = sum(e[2] for e in res1)
    w2 = sum(e[2] for e in res2)

    if len(res1) == 0:
        no_builded += 1
        continue

    if (len(res1) != len(res2)) or (len(res1) != n-1):
        errors += 1
        
    if w1 != w2:
        errors += 1

    if w1 == w2:
        time1 = t1-t0
        time2 = t2-t1

        x += [n]
        f1 += [math.log(time1, n)]
        f2 += [math.log(time2, n)]

print("Ошибок:", errors)
print("Невозможно построить дерево:", no_builded)
print("Время алгоритма Эдмондса (наносекунд) при n = " + str(n_max) + ":", time1)
print("Время алгоритма MSF      (наносекунд) при n = " + str(n_max) + ":", time2)
print("log(time, n) для алгоритма Эдмондса:", f1[-1])
print("log(time, n) для алгоритма MSF     :", f1[-1])

plt.plot(x, f1, label='Edmonds')
plt.plot(x, f2, label='MSF')
plt.legend()
plt.show()
```