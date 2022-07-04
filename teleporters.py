"""
Teleporters

The president has decided that winters have gotten too long and by next winter, the beloved tunnels connecting the entire campus should be accessible once again. 
Unfortunately, all the old tunnels running under the quad have become unusable and new ones need to be built. Of course, this should be kept economical and 
financially responsible. An engineering firm has provided all possible tunnels that could be dug, and of course the price tag for each of them. 
In a wild revelation, Fermilab announced that they now have a working teleporter, but it only works for short distances. The engineering firm has provided estimates 
for installing these teleporters in various building around campus (but not all). The president wants all buildings to be connected by at least one path, but also 
for the entire project to cost as low as possible. To that end, you need to find the best set of tunnels and (maybe) teleporters to connect the entire campus for 
the next winter.

Input: In the first line there are three integers $N$, $K$, $M$, which correspond to the number of buildings, the number of buildings where a teleporter can be installed and the number of possible tunnels between buildings.
In the next $K$ lines there are two integers, $i$ and $B[i]$, meaning that a teleporter can be installed in building $i$ with cost $B[i]$.
Finally, the next $M$ lines contain three integers $i$, $j$, $c[i, j]$, which denote that there is a proposed tunnel between buildings $i$ and $j$ with cost $c[i, j]$.

Output: One line with a single integer, the minimum cost for the entire network.
"""

from collections import defaultdict


def solve(N, K, M, teleporters, edges):
    g1 = Graph(N)
    g1.graph = edges
    min_cost_tunnels = g1.kruskal_algo()
    
    g2 = Graph(N + 1)
    for node, weight in teleporters:
        edges.append([node - 1, N, weight])
    g2.graph = edges
    min_cost_with_teleporters = g2.kruskal_algo()

    if min_cost_tunnels < min_cost_with_teleporters:
        return min_cost_tunnels
    else:
        return min_cost_with_teleporters


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    '''def add_edge(self, u, v, w):
        self.graph.append([u, v, w])'''

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

#  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        min_cost = 0
        for u, v, weight in result:
            min_cost += weight
        return min_cost


def read_input():
    N, K, M = [int(i) for i in input().split()]
    teleporters = [[int(i) for i in input().split()] for _ in range(K)]
    edges = []
    for i in range(M):
        u, v, c = [int(i) for i in input().split()]
        edges.append([u-1,v-1,c])
    return N, K, M, teleporters, edges


def main():
    N, K, M, teleporters, edges = read_input()
    cost = solve(N, K, M, teleporters, edges)
    print(cost)


if __name__ == '__main__':
    main()
