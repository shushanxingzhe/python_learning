import copy
from math import inf as X



distanceMap = [
    [0,	4,	X,	2,	X,  X,  X],
    [4,	0,	4,	1,	X,  1,  X],
    [X,	4,	0,	1,	3,  1,  X],
    [2,	1,	1,	0,	7,  X,  X],
    [X,	X,	3,	7,	0,  2,  2],
    [X, 1,  1,  X,  2,  0,  X],
    [X, X,  X,  X,  2,  X,  0]
]



def prim(Map):
    localMap = copy.deepcopy(Map)
    n = len(localMap)
    V = []
    U = list(range(n))
    # init point
    V.append(U.pop())
    E = []

    for i in range(n-1):
        minEdge = X
        start =0
        stop = 0
        for j in V:
            for k in U:
                if localMap[j][k] < minEdge:
                    minEdge = localMap[j][k]
                    start = j
                    stop = k

        V.append(U.pop(U.index(stop)))
        E.append([start,stop])
    return E


result = prim(distanceMap)
for start,stop in result:
    print('From ' + str(start) + '  To  ' + str(stop))

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
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


T = nx.minimum_spanning_tree(G, algorithm='prim')
print(T.edges(data=True))
nx.draw_networkx_edges(G, pos, edgelist=T.edges(), edge_color='r')

plt.show()