# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]


def shiftvert(v, n):
    return ((v - 1) * n) + 1


def printEquisatisfiableSatFormula(n, m, edges):

    missing_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if [i + 1, j + 1] not in edges and [j + 1, i + 1] not in edges:
                missing_edges.append([i + 1, j + 1])

    c = 2 * n + n * n * (n - 1) + 2 * len(missing_edges) * (n - 1)
    v = n * n * 2
    print(c, v)

    # Each vertex belongs to a path
    for i in range(n):
        u = shiftvert(i + 1, n)
        verticies = list(range(u, u + n))
        verticies.append(0)
        print(' '.join(map(str, verticies)))

    # Each vertex appears just once in a path.
    for v in range(n):
        u = shiftvert(v + 1, n)
        for i in range(n):
            for j in range(u + i + 1, u + n):
                print(-u - i, -j, 0)

    # Each position in a path is occupied by some vertex.
    for i in range(n):
        verticies = list(range(i + 1, n * n + 1, n))
        verticies.append(0)
        print(' '.join(map(str, verticies)))

    # No two vertices occupy the same position of a path
    for v in range(n):
        verticies = list(range(v + 1, n * n + 1, n))
        for idx, i in enumerate(verticies):
            for j in verticies[idx + 1:]:
                print(-i, -j, 0)

    # Two successive vertices on a path must be connected by an edge
    for e in missing_edges:
        u = shiftvert(e[0], n)
        v = shiftvert(e[1], n)
        for i in range(n - 1):
            print(-u - i, -v - i - 1, 0)
            print(-v - i, -u - i - 1, 0)










printEquisatisfiableSatFormula(n, m, edges)
