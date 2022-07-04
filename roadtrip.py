#!/usr/bin/env pypy3
'''In the future, all cars are electric. More-
over, for long journeys, instead of charging your car you can just grab a new battery from one of the charging
stations. Because of EU regulations all battery manufacturers use the same adapters, but because of different voltages
and capacities, each battery can make the car go at different speeds until they run out. Jonathan is going on (another)
trip, this time from Chicago to New York, and needs your help to decide how he will get there. Jonathan starts in
Chicago (node 1) and needs to decide at which charging stations he needs to change batteries to get to New York
(node N). Formally, you are given a graph with N nodes, each of which have a battery that can move Jonathan up to
distance ci with speed si , and M edges (roads) each of which has a length d(u, v). Testcases can be found here.
Input: In the first line you are given two integers N, M. In each of the next N lines there are two integers, ci ,
si . M lines follow, each with three integers, u, v, d(u, v).
Output: Your program should output a single floating point number with exactly six points of precision, the
time it takes Jonathan to go from node 1 to node N.
Limits:
N ≤200
M ≤ N2
T ≤1s'''
from collections import defaultdict
import heapq
import math

def solve(N, M, batteries, dists):
    graph = create_graph(batteries, dists)
    least_time = dijkstras(N, graph)
    return least_time

def create_graph(batteries, dists):
    G = defaultdict(list)
    for start, end, dist in dists:
        if batteries[start - 1][0] >= dist:
            G[start - 1].append((end - 1, dist/batteries[start - 1][1]))
    return G

def dijkstras(N, graph):
    visited = [False for _ in range(N)]
    dists = [math.inf for i in range(N)]
    dists[0] = 0
    pq = [(dists[0], 0)]
    
    while len(pq) > 0:
        dist, u = heapq.heappop(pq)
        visited[u] = True
        for end_node, time in graph[u]:
            if visited[end_node] == False:
                maybe_dist = dist + time
                if maybe_dist < dists[end_node]:
                    dists[end_node] = maybe_dist
                    heapq.heappush(pq, (dists[end_node], end_node))

    return dists[N - 1]


def read_input():
    N, M = [int(i) for i in input().split()]
    batteries = [[int(i) for i in input().split()] for _ in range(N)]
    dists = [[int(i) for i in input().split()] for _ in range(M)]
    return N, M, batteries, dists


def main():
    N, M, batteries, dists = read_input()
    t = solve(N, M, batteries, dists)
    print(f'{t:.6f}')


if __name__ == '__main__':
    main()
