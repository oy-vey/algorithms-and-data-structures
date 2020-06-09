# python3

n = 1618
reads = []
for _ in range(n):
    reads.append(input())


def getMaxOverlap(i, reads, visited):
    max_overlap = -1
    max_idx = -1
    match = ""
    read_len = len(reads[i])
    for j, pattern in enumerate(reads):
        if i == j or visited[j]:
            continue
        else:
            for s in range(read_len):
                if (read_len - s) > max_overlap:
                    if reads[i].endswith(reads[j][:read_len-s]):
                        max_overlap = (read_len - s)
                        max_idx = j
                        match = reads[j][read_len-s:]
                        break
                else:
                    break
    return max_idx, match


def trimResult(result, max_border):
    for s in range(max_border):
        if result.endswith(result[:max_border-s]):
            result = result[:-max_border+s]
            return result
    return result


step = 0
i = 0
result = ""
visited = [0] * n
visited[i] = 1
match = reads[i]
result += match
while step < n:
    max_idx, match = getMaxOverlap(i, reads, visited)
    result += match
    visited[max_idx] = 1
    i = max_idx
    step += 1

result_trimmed = trimResult(result, 100)
#result_trimmed = trimResult('ACGTTCGAACG', 3)
print(result_trimmed)
