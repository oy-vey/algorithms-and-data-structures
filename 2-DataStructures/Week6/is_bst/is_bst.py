#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


mx = None

def IsBinarySearchTree(tree):
  if len(tree) in (0,1):
    return True

  def inOrderTraversal(tree, i):
    global mx
    if i == -1:
      return True

    if not inOrderTraversal(tree, tree[i][1]):
      return False

    if mx is None or mx < tree[i][0]:
      mx = tree[i][0]
    else:
      return False

    if not inOrderTraversal(tree, tree[i][2]):
      return False

    return True

  if inOrderTraversal(tree, 0):
    return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
