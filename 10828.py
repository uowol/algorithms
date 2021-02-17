import sys
# from collections import deque
# import heapq

# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

stack = []
for i in range(n):
    ipt = input().split()
    
    if len(ipt) == 2: # push
        stack.append(ipt[1])
    else: ipt = ipt[0]

    if ipt == 'size': print(len(stack))
    if ipt == 'pop': 
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    if ipt == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    if ipt == 'top':
        if len(stack) == 0: print(-1)
        else: print(stack[len(stack) - 1])
    