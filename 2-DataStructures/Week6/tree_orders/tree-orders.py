# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []

    def inOrderTraversal(tree):
      if tree == -1:
          return
      inOrderTraversal(self.left[tree])
      self.result.append(self.key[tree])
      inOrderTraversal(self.right[tree])

    inOrderTraversal(0)
    return self.result

  def preOrder(self):
    self.result = []

    def preOrderTraversal(tree):
      if tree == -1:
          return
      self.result.append(self.key[tree])
      preOrderTraversal(self.left[tree])
      preOrderTraversal(self.right[tree])

    preOrderTraversal(0)
                
    return self.result

  def postOrder(self):
    self.result = []

    def postOrderTraversal(tree):
      if tree == -1:
        return
      postOrderTraversal(self.left[tree])
      postOrderTraversal(self.right[tree])
      self.result.append(self.key[tree])

    postOrderTraversal(0)
                
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
