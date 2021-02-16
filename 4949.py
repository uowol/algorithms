import sys
from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def check(s):
    q = deque([])
    for c in list(s):
        if c == '[':
            q.append(1)
        if c == '(':
            q.append(0)
        if c == ']':
            if len(q) == 0 or q[len(q)-1] != 1:
                return False
            q.pop()
        if c == ')':
            if len(q) == 0 or q[len(q)-1] != 0:
                return False
            q.pop()
    if len(q) > 0:
        return False
    return True
        
        

ipt = input().rstrip()
while ipt != '.':
    if check(ipt):
        print('yes')
    else:
        print('no')
    ipt = input().rstrip()