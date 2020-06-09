# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]


def shiftvert(v):
    return ((v - 1) * 3) + 1


def printEquisatisfiableSatFormula(n, m, edges):
    c = (n * 4) + (m * 3)
    v = n * 3 * 2
    print(c, v)
    i = 1
    while i <= n:
        u = shiftvert(i)
        print(u, u + 1, u + 2, 0)
        print(-u, -u - 1, 0)
        print(-u, -u - 2, 0)
        print(-u - 1, -u - 2, 0)

        i += 1

    for e in edges:
        u = shiftvert(e[0])
        v = shiftvert(e[1])
        print(-u, -v, 0)
        print(-u - 1, -v - 1, 0)
        print(-u - 2, -v - 2, 0)


printEquisatisfiableSatFormula(n, m, edges)
