#Uses python3

import sys

def dfs(v):
    used[v] = 1
    for w in adj[v]:
        if not used[w]:
            dfs(w)
    order.insert(0, v)


def toposort(adj):
    global used
    global order
    used = [0] * len(adj)
    order = []
    for v in range(0, len(adj)):
        if not used[v]:
            dfs(v)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

