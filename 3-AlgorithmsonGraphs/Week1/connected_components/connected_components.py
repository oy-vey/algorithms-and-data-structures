#Uses python3

import sys


def number_of_components(adj):
    global visited
    visited = [0] * (len(adj))
    global cc
    cc = 0
    for v in range(0, len(adj)):
        if not visited[v]:
            explore(v)
            cc += 1
    return cc

def explore(v):
    visited[v] = 1
    for w in adj[v]:
        if not visited[w]:
            explore(w)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
