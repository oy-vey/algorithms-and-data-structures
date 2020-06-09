#Uses python3

import sys


def BellmanFord(adj, S, cost):
    dist = list()
    prev = list()
    inf = 0
    for c in cost:
        inf += sum(c)
    inf += 1
    for u in range(0, len(adj)):
        dist.append(inf)
        prev.append(None)
    dist[S] = 0

    for iter in range(0, len(adj)):
        for u, out in enumerate(adj):
            for i, v in enumerate(out):
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    prev[v] = u
    for u, out in enumerate(adj):
        for i, v in enumerate(out):
            if dist[v] > dist[u] + cost[u][i]:
                return 1

    return 0

def negative_cycle(adj, cost):
    return BellmanFord(adj, 0, cost)


if __name__ == '__main__':
    input = sys.stdin.read()
    # with open('test', 'r') as f:
    #     input = f.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
