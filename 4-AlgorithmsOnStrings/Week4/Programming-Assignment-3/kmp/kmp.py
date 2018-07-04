# python3
import sys

def computePrefixFunction(P):
  Plen = len(P)
  s = [0] * Plen
  s[0] = 0
  border = 0
  for i in range(1, Plen):
    while border > 0 and P[i] != P[border]:
      border = s[border - 1]
    if P[i] == P[border]:
      border += 1
    else:
      border = 0
    s[i] = border
  return s


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  S  = pattern + '$' + text
  s = computePrefixFunction(S)
  result = []
  Plen = len(pattern)
  Slen = len(S)
  for i in range(Plen + 1, Slen):
    if s[i] == Plen:
      result.append(i - 2*Plen)
  # Implement this function yourself
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

