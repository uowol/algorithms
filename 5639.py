import sys
# from collections import deque
# from itertools import combinations
# import heapq

sys.setrecursionlimit(20_000)

def input():
    return sys.stdin.readline().rstrip()

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def postorder(self):
        travelsal = []
        if self.left: travelsal += self.left.postorder()
        if self.right: travelsal += self.right.postorder()
        travelsal.append(self.data)
        return travelsal

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            self.addNode(self.root, key)

    def addNode(self, cur, key):
        if key < cur.data:
            if cur.left:
                self.addNode(cur.left, key)
            else:
                cur.left = Node(key)
        elif key > cur.data:
            if cur.right:
                self.addNode(cur.right, key)
            else:
                cur.right = Node(key)

    def postorder(self):
        if self.root: return self.root.postorder()
        return []
    
bt = BinaryTree()
while True:
    try:
        key = int(input())
        bt.insert(key)
    except:
        break

for output in bt.postorder():
    print(output)
