import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

q = deque([i+1 for i in range(n)])

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.pop())