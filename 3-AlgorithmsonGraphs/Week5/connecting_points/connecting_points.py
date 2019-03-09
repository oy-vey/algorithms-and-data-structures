#Uses python3
import sys
import math


def find(x):
    if sets[x] == x:
        return x
    else:
        sets[x] = find(sets[x])
        return sets[x]

def minimum_distance(x, y):
    result = 0.
    global sets
    global rank
    rank = [0] * len(x)
    sets = list(range(0, len(x)))
    edges = list()
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
            result += edge[0]
            if rank[i_id] > rank[j_id]:
                sets[j_id] = i_id
            else:
                sets[i_id] = j_id
                if rank[i_id] == rank[j_id]:
                    rank[j_id] += 1
    return result


if __name__ == '__main__':
    # input = sys.stdin.read()
    with open('test', 'r') as f:
        input = f.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))