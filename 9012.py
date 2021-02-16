import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def check(s):
    q = deque([])
    for c in list(s):
        if c == '(':
            q.append(0)
        if c == ')':
            if len(q) == 0 or q[len(q)-1] != 0:
                return False
            q.pop()
    if len(q) > 0:
        return False
    return True
        
n = int(input())

for _ in range(n):
    ipt = input().rstrip()
    if check(ipt):
        print('YES')
    else:
        print('NO')