#Uses python3

import sys

sys.setrecursionlimit(200000)

def DFS(adj):
    global clock
    global pre
    global post
    global visited
    # pre = [0] * len(adj)
    # post = [0] * len(adj)
    # clock = 0
    # visited = [0] * len(adj)
    for v in range(0,len(adj)):
        if not visited[v]:
            explore(v, adj)

def explore(v, adj):
    global visited
    visited[v] = 1
    previsit(v)
    for w in adj[v]:
        if not visited[w]:
            explore(w, adj)
    postvisit(v)

def previsit(v):
    global pre
    global clock
    pre[v] = clock
    clock += 1

def postvisit(v):
    global post
    global clock
    post[v] = clock
    clock += 1


def Reverse(adj):
    adj_rev = [[] for i in range(len(adj))]
    for v, edge in enumerate(adj):
        for w in edge:
            adj_rev[w].append(v)
    return adj_rev

def number_of_strongly_connected_components(adj):
    global clock
    global pre
    global post
    global visited
    pre = [0] * len(adj)
    post = [0] * len(adj)
    clock = 0
    visited = [0] * len(adj)
    result = 0
    DFS(Reverse(adj))
    rev_post = [x for _,x in sorted(zip(post,range(0, len(adj))), reverse=True)]
    pre = [0] * len(adj)
    post = [0] * len(adj)
    clock = 0
    visited = [0] * len(adj)
    for v in rev_post:
        if not visited[v]:
            explore(v, adj)
            result += 1
    return result

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
    print(number_of_strongly_connected_components(adj))
