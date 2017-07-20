# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    W = capacity
    value = 0.
    ProfitPerUnit = list(zip(weights, values))
    ProfitPerUnitSrtd = sorted(ProfitPerUnit, key=lambda profit: (profit[1]/profit[0]), reverse=True)
    for i in range(0, len(ProfitPerUnitSrtd)):
        if W == 0:
            return(value)
        a = min(ProfitPerUnitSrtd[i][0], W)
        value += a * ProfitPerUnitSrtd[i][1] / ProfitPerUnitSrtd[i][0]
        #ProfitPerUnitSrtd[i][0] -= a
        W -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
