#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    tree[0] = dict()
    n = 0
    for pattern in patterns:
        currentNode = 0
        for i in range(0,len(pattern)):
            currentSymbol = pattern[i]
            if currentSymbol in tree[currentNode].keys():
                currentNode = tree[currentNode][currentSymbol]
            else:
                tree[currentNode][currentSymbol] = n + 1
                n += 1
                currentNode = n
                if i != len(pattern) - 1:
                    tree[currentNode] = dict()
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
