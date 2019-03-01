#Uses python3

import sys
import queue



def Dijkstra(adj, s, cost, t):
    dist = list()
    prev = list()
    inf = 0
    for c in cost:
        inf += sum(c)
    inf += 1
    for u in range(0, len(adj)):
        dist.append(inf)
        prev.append(None)
    dist[s] = 0
    H = queue.PriorityQueue()
    for i, d in enumerate(dist):
        H.put((d, i))
    processed = set()
    while not H.empty():
        u = H.get()[1]
        if u in processed:
            pass
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                H.put((dist[v], v))
                processed.add(v)


    if dist[t]< inf:
        return dist[t]
    else:
        return -1

def distance(adj, cost, s, t):
    return Dijkstra(adj, s, cost, t)


if __name__ == '__main__':
    # input = sys.stdin.read()
    with open('test', 'r') as f:
        input = f.read()
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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
