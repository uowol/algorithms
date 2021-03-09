import sys
# from collections import deque
# from itertools import combinations
# import heapq

# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l+r+1

    def depth(self):
        leftDepth = self.left.depth() if self.left else 0
        rightDepth = self.right.depth() if self.right else 0
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1

    def inorder(self):
        travelsal = []
        if self.left: travelsal += self.left.inorder()
        travelsal += self.data
        if self.right: travelsal += self.right.inorder()
        return travelsal

    def preorder(self):
        travelsal = []
        travelsal += self.data
        if self.left: travelsal += self.left.preorder()
        if self.right: travelsal += self.right.preorder()
        return travelsal

    def postorder(self):
        travelsal = []
        if self.left: travelsal += self.left.postorder()
        if self.right: travelsal += self.right.postorder()
        travelsal += self.data
        return travelsal

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root: return self.root.size()
        return 0

    def depth(self):
        if self.root: return self.root.depth()
        return 0

    def inorder(self):
        if self.root: return self.root.inorder()
        return []

    def preorder(self):
        if self.root: return self.root.preorder()
        return []

    def postorder(self):
        if self.root: return self.root.postorder()
        return []
    
n = int(input())
alphabet = [chr(65 + i) for i in range(26)]
node = [Node(alphabet[i]) for i in range(n)]
tree = BinaryTree(node[0])

for i in range(n):
    root, l, r = map(lambda x: ord(x) - 65, input().split())
    if l >= 0:
        node[root].left = node[l]
    if r >= 0:
        node[root].right = node[r]

print(''.join(tree.preorder()))
print(''.join(tree.inorder()))
print(''.join(tree.postorder()))