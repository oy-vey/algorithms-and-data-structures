#Uses python3

import sys

def acyclic(adj):
    global has_cycle
    has_cycle = [0]
    global visited
    visited = [0] * (len(adj))
    for v in range(0, len(adj)):
        if not visited[v]:
            explore(v)
        if has_cycle[0] == 1:
            return 1
    return 0

def explore(v):
    visited[v] = 1
    for w in adj[v]:
        if not visited[w]:
            explore(w)
        else:
            has_cycle[0] = 1
            break
    visited[v] = 0

if __name__ == '__main__':
    input = sys.stdin.read()
    # with open('test','r') as f:
    #     input = f.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
