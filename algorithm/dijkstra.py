import copy
from math import inf as X

start = 1
stop = 4

distanceMap = [
    [0,	4,	X,	2,	X,  X,  X],
    [4,	0,	4,	1,	X,  1,  X],
    [X,	4,	0,	1,	3,  1,  X],
    [2,	1,	1,	0,	7,  X,  X],
    [X,	X,	3,	7,	0,  2,  2],
    [X, 1,  1,  X,  2,  0,  X],
    [X, X,  X,  X,  2,  X,  0]
]

def dijkstra(Map,start,stop):
    localMap = copy.deepcopy(Map)
    n = len(localMap)
    S = [0] * n
    Path = [str(start)] * n

    sl = [0] * n

    for i in range(n):
        l = start
        mdis = X
        for j in range(n):
            if S[j] == 0 and localMap[start][j] < mdis:
                mdis = localMap[start][j]
                l = j

        sl[l] = mdis
        S[l] = 1

        for k in range(n):
            if localMap[start][l] + localMap[l][k] < localMap[start][k]:
                localMap[start][k] = localMap[start][l] + localMap[l][k]
                Path[k] = Path[l] + '->' + str(l)

        if l == stop:
            print(sl[stop], ':', Path[stop] + '->' + str(stop))

def dijkstra_all(Map,start):
    localMap = copy.deepcopy(Map)
    n = len(localMap)
    S = [0] * n
    Path = [str(start)] * n

    sl = [0] * n

    for i in range(n):
        l = start
        mdis = X
        for j in range(n):
            if S[j] == 0 and localMap[start][j] < mdis:
                mdis = localMap[start][j]
                l = j

        sl[l] = mdis
        S[l] = 1

        for k in range(n):
            if localMap[start][l] + localMap[l][k] < localMap[start][k]:
                localMap[start][k] = localMap[start][l] + localMap[l][k]
                Path[k] = Path[l] + '->' + str(l)
    for i in range(n):
        print(sl[i], ':', Path[i] + '->' + str(i))


dijkstra(distanceMap,start,stop)
dijkstra_all(distanceMap,start)

import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_weighted_edges_from([
                                (0,1,4),
                                (0,3,2),
                                (1,2,4),
                                (1,3,1),
                                (1,5,1),
                                (2,3,1),
                                (2,4,3),
                                (2,5,1),
                                (3,4,7),
                                (4,5,2),
                                (4,6,2)
                               ])

pos=nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, poswith_labels=True, font_weight='bold')

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos ,edge_labels=labels)
print(nx.algorithms.shortest_paths.weighted.dijkstra_path(G, source=start, target=stop))
print(nx.algorithms.shortest_paths.weighted.dijkstra_path_length(G, source=start, target=stop))

plt.show()