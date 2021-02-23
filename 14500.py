import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

h, w = map(int, input().split())

khan = [None for _ in range(h)]
for i in range(h):
    khan[i] = list(map(int, input().split()))

stack = deque([])
def dfs(visit, cnt):
    global khan
    x, y = stack.pop()
    if cnt == 4:
        return khan[y][x]
    if x > 0 and not visit[y][x-1]

