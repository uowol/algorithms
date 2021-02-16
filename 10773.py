import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

q = deque([])

for _ in range(n):
    q.append(int(input()))
    if q[len(q)-1] == 0:
        q.pop()
        q.pop()

if len(q)==0:print(0)
else:
    print(sum(q))