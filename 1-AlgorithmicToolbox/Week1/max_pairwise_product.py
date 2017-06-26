# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)


max1 = -1
max1_ix = -1
max2 = -1


for i in range(0, n):
    if a[i] > max1:
        max1 = a[i]
        max1_ix = i

for j in range(0, n):
    if a[j] > max2 and j != max1_ix:
        max2 = a[j]

result = max1 * max2
print(result)
