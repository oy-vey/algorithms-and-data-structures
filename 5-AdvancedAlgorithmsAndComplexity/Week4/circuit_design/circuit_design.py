#Uses python3

import sys
import threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

n, m = map(int, input().split())
clauses = [list(map(int, input().split())) for i in range(m)]

n_impl = 2 * n
m_impl = 2 * m
clauses_impl = []
for c in clauses:
    clauses_impl.append([-c[1], c[0]])
    clauses_impl.append([-c[0], c[1]])



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

def explore(v, adj, scc=1):
    global visited
    visited[v] = scc
    previsit(v)
    for w in adj[v]:
        if not visited[w]:
            explore(w, adj, scc)
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
    num_of_scc = 1
    DFS(Reverse(adj))
    rev_post = [x for _,x in sorted(zip(post,range(0, len(adj))), reverse=True)]
    #print(rev_post)
    pre = [0] * len(adj)
    post = [0] * len(adj)
    clock = 0
    visited = [0] * len(adj)
    for v in rev_post:
        if visited[v] == 0:
            explore(v, adj, num_of_scc)
            num_of_scc += 1

    #print(visited)
    for v in range(n):
        if visited[v] == visited[v+n]:
            return None
    sccs = [[] for _ in range(n_impl)]
    for v in range(n_impl):
        sccs[visited[v] - 1].append(v)
    result = [-1] * len(adj)
    for scc in range(num_of_scc - 1):
        for v in sccs[scc]:
            if result[v] == -1:
                #print(v+1)
                if v < n:
                    result[v] = 1
                    result[v + n] = 0
                else:
                    result[v] = 1
                    result[v - n] = 0


    return result


def main():


    adj = [[] for _ in range(n_impl)]
    for (a, b) in clauses_impl:
        if a < 0:
            a = -a + n
        if b < 0:
            b = -b + n
        adj[a - 1].append(b - 1)



    #print(number_of_strongly_connected_components(adj))
    result = number_of_strongly_connected_components(adj)
    if result is None:
        print("UNSATISFIABLE")

    # if -1 in result:
    #     exit()
    else:
        print("SATISFIABLE")
        print(" ".join(str(i+1 if result[i] == 1 else -i-1) for i in range(n)))


threading.Thread(target=main).start()