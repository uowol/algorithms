# N-Queen

def input():
    return sys.stdin.readline().rstrip()

import sys
sys.setrecursionlimit(10**6)
from collections import deque

N = int(input())

def dfs(queen, N):    
    if len(queen) == N: return 1
    cnt = 0
    candidate = [i for i in range(N)]
    for i in range(len(queen)):
        if queen[i] in candidate: candidate.remove(queen[i])
        dist = len(queen) - i
        if queen[i] + dist in candidate: candidate.remove(queen[i] + dist)
        if queen[i] - dist in candidate: candidate.remove(queen[i] - dist)
    for i in range(len(candidate)):
        cnt += dfs(queen+[candidate[i]], N)
    return cnt
ans = 0
for i in range(N):
    ans += dfs([i], N)
print(ans)
