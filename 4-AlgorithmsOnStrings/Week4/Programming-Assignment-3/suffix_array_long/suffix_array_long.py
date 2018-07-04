# python3
import sys


def getIND(char):
  if char == 'A':
    return 1
  elif char == 'C':
    return 2
  elif char == 'G':
    return 3
  elif char == 'T':
    return 4
  else:
    return 0

def SortCharacters(S):
  Slen = len(S)
  order = [-1] * Slen
  count = [0] * 5
  for i in range(0, Slen):
    count[getIND(S[i])] += 1
  for j in range(1, 5):
    count[j] += count[j-1]
  for i in range(Slen - 1, -1, -1):
    c = S[i]
    count[getIND(c)] -= 1
    order[count[getIND(c)]] = i
  return order


def ComputeCharClasses(S, order):
  Slen = len(S)
  cls = [-1] * Slen
  cls[order[0]] = 0
  for i in range(1, Slen):
    if S[order[i]] != S[order[i-1]]:
      cls[order[i]] = cls[order[i-1]] + 1
    else:
      cls[order[i]] = cls[order[i - 1]]
  return cls



def SortDoubled(S, L, order, cls):
  Slen = len(S)
  count = [0] * Slen
  newOrder = [-1] * Slen
  for i in range(0, Slen):
    count[cls[i]] += 1
  for j in range(1, Slen):
    count[j] += count[j-1]
  for i in range(Slen - 1, -1,-1):
    start = (order[i] - L + Slen) % Slen
    cl = cls[start]
    count[cl] -= 1
    newOrder[count[cl]] = start
  return newOrder

def UpdateClasses(newOrder, cls, L):
  n = len(newOrder)
  newClass = [-1] * n
  newClass[newOrder[0]] = 0
  for i in range(1, n):
    cur = newOrder[i]
    prev = newOrder[i-1]
    mid = cur + L
    midPrev = (prev + L) % n
    if cls[cur] != cls[prev] or cls[mid] != cls[midPrev]:
      newClass[cur] = newClass[prev] + 1
    else:
      newClass[cur] = newClass[prev]
  return newClass

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """

  order = SortCharacters(text)
  cls = ComputeCharClasses(text, order)
  L = 1
  Slen = len(text)
  while L < Slen:
    order = SortDoubled(text, L, order, cls)
    cls = UpdateClasses(order,cls, L)
    L = L * 2
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
