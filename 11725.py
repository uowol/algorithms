import sys
# from collections import deque
# import heapq
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
# parent[1] = 1
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(before, node):
    parent[node] = before
    for node_next in tree[node]:
        if not parent[node_next]:
            bfs(node, node_next)
bfs(1, 1)
# print(tree, parent)
for node in range(2, n+1):
    print(parent[node])