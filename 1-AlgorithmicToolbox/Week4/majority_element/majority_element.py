# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    maxl = get_majority_element(a, left, (left + right) // 2)
    maxr = get_majority_element(a, (left + right) // 2,  right)
    l = []
    if maxl >= 0: l.append(maxl)
    if maxr >= 0: l.append(maxr)
    for item in l:
        CurrentElement = item
        count = 0
        for j in range(left, right):
            if a[j] == CurrentElement:
                count += 1
                if count > (right - left) // 2:
                    return item
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
