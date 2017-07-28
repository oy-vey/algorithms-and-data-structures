# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    maxl = get_majority_element(a, left, (left + right) // 2)
    maxr = get_majority_element(a, (left + right) // 2,  right)
    if maxl == maxr:
        return [maxl]
    #if n == len(a) and ()
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
