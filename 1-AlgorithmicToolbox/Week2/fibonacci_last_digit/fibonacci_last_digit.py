# Uses python3


def get_fibonacci_last_digit(n):
    fibs = [None] * max(n + 1, 2)
    fibs[0] = 0
    fibs[1] = 1

    for i in range(2, n + 1):
        fibs[i] = (fibs[i-1] + fibs[i-2]) % 10
    return fibs[n]

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
