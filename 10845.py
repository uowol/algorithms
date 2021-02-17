import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

q = deque([])

for i in range(n):
    ipt = input().split()
    
    if len(ipt) == 2: # push
        q.append(ipt[1])
    else: ipt = ipt[0]

    if ipt == 'size': print(len(q))
    if ipt == 'empty':
        if len(q) == 0: print(1)
        else: print(0)
    elif len(q) == 0:
        print(-1)
    else:
        if ipt == 'pop': 
            print(q.popleft())
        if ipt == 'front': 
            print(q[0])
        if ipt == 'back':
            print(q[len(q)-1])
    