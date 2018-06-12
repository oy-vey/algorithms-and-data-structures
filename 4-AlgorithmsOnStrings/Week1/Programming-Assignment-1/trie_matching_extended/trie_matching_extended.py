# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4


def TrieMatching(text, n, patterns):
	result = []
	trie = build_trie(patterns)
	i = 0
	while text:
		if PrefixTrieMatching(text, trie):
			result.append(i)
		text = text[1:]
		i += 1
	return result

def PrefixTrieMatching(text, trie):
	i = 0
	symbol = text[i]
	v = 0
	while(i < len(text)):
		if v not in trie.keys() or trie[v].get('$'):
			return True
		elif symbol in trie[v].keys():
			v = trie[v][symbol]
			try:
				symbol = text[i + 1]
				i += 1
			except:
				symbol = None
		else:
			return False

def build_trie(patterns):
	tree = dict()
	tree[0] = {} #{'IsFinal':0}
	n = 0
	for pattern in patterns:
		currentNode = 0
		for i in range(0,len(pattern)):
			currentSymbol = pattern[i]
			if currentSymbol in tree[currentNode].keys():
				currentNode = tree[currentNode][currentSymbol]
				#tree[currentNode]['IsFinal'] = 1 if i == len(pattern) - 1 else 0
			else:
				tree[currentNode][currentSymbol] = n + 1
				n += 1
				currentNode = n
				tree[currentNode] = dict()
				#tree[currentNode]['IsFinal'] = 1 if i == len(pattern) - 1 else 0
			if i == len(pattern) - 1:
				tree[currentNode]['$'] = n + 1
				n += 1
				currentNode = n
				tree[currentNode] = dict()
	return tree


text = sys.stdin.readline().strip ()
n = int(sys.stdin.readline().strip ())
patterns = []
for i in range(n):
 	patterns += [sys.stdin.readline().strip()]

ans = TrieMatching(text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')