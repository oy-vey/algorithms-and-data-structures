#Uses python3
import sys
import math


def find(x):
    if sets[x] == x:
        return x
    else:
        sets[x] = find(sets[x])
        return sets[x]

def clustering(x, y, k):
    global sets
    global rank
    sets = list(range(0, len(x)))
    rank = [0] * len(x)
    edges = list()
    edges_mst = list()
    for i in range(0, n):
        weights = list()
        for j in range(i + 1, n):
            w = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            weights.append((w, i, j))
        edges += weights
    edges.sort()
    for edge in edges:
        i_id = find(sets[edge[1]])
        j_id = find(sets[edge[2]])
        if i_id != j_id:
            edges_mst.append(edge)
            if rank[i_id] > rank[j_id]:
                sets[j_id] = i_id
            else:
                sets[i_id] = j_id
                if rank[i_id] == rank[j_id]:
                    rank[j_id] += 1
    return edges_mst[-k+1][0]


if __name__ == '__main__':
    # input = sys.stdin.read()
    with open('test', 'r') as f:
        input = f.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
