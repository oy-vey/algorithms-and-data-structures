# Uses python3
def calc_fib(n):
    fibs = [None] * max(n + 1, 2)
    fibs[0] = 0
    fibs[1] = 1

    for i in range(2, n + 1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]

n = int(input())
print(calc_fib(n))
