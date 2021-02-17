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
        if ipt[0] == 'push_front':
            q.appendleft(ipt[1])
        else:
            q.append(ipt[1])
    else: ipt = ipt[0]

    if ipt == 'size': print(len(q))
    elif ipt == 'empty':
        if len(q) == 0: print(1)
        else: print(0)
    elif len(q) == 0:
        print(-1)
    else:
        if ipt == 'pop_front': 
            print(q.popleft())
        if ipt == 'pop_back': 
            print(q.pop())
        if ipt == 'front': 
            print(q[0])
        if ipt == 'back':
            print(q[len(q)-1])
    