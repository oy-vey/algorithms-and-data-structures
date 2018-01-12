# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                tree = dict()
                for vertex in range(-1, self.n):
                    tree[vertex] = []
                for vertex in range(self.n):
                    tree[self.parent[vertex]].append(vertex)
                return tree


def compute_height(tree, v = -1):
    if not tree[v]:
        return 0
    max = 0
    for child in tree[v]:
        height = compute_height(tree, child)
        if  height > max:
            max = height
    return 1 + max



def main():
  treeheight = TreeHeight()
  tree = treeheight.read()
  print(compute_height(tree))
  #print(tree)

threading.Thread(target=main).start()
