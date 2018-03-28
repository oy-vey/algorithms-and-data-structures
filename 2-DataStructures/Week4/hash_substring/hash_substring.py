# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))


def PolyHash(S, p, x):
    hash = 0
    for c in reversed(S):
        hash += (hash * x + ord(c)) % p
    return hash

def PrecomputeHashes(T, lenP, p, x):
    lenT = len(T)
    H = [None] * (lenT - lenP + 1)
    S = T[lenT - lenP:lenT - 1]
    H[lenT-lenP] = PolyHash(S, p, x)
    y = 1
    for i in range(1, lenP + 1):
        y = (y * x) % p
    for i in range(lenT - lenP - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + lenP]))
    return H

def get_occurrences(pattern, text):
    lenP = len(pattern)
    lenT = len(text)
    p = 10 ** 8
    x = random.randint(0, p - 1)
    result = []
    pHash = PolyHash(pattern, p, x)
    H = PrecomputeHashes(text, lenP, p, x)
    for i in range(0, lenT - lenP + 1):
        if pHash != H[i]:
            continue
        if text[i:i+lenP-1] == pattern:
            result.append(i)
        return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

