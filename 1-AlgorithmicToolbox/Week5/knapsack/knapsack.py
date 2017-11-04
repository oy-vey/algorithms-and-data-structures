# Uses python3
import sys

def optimal_weight(W, weights):
    # write your code here
    n = len(weights)
    value = []
    for i in range(0,W + 1):
        value.append([])
        for j in range(0,n + 1):
            if j == 0:
                value[i].append(0)
            elif i == 0:
                value[i].append(0)
            else:
                value[i].append(-1)

    for i in range(1,n+1):
        for w in range(1,W+1):
            value[w][i] = value[w][i-1]
            if weights[i-1] <= w:
                val = value[w-weights[i-1]][i-1] + weights[i-1]
                if value[w][i] < val:
                    value[w][i] = val
    return value[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
