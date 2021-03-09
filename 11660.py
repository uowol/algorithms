import sys
# from collections import deque
# import heapq
# sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

dp = [None for _ in range(n)]
for i in range(n):
    dp[i] = list(map(int, input().split()))
    for j in range(1, n):
        dp[i][j] += dp[i][j-1]
# for s in dp: print(s)

for _ in range(m):
    si, sj, ei, ej = map(lambda x: int(x)-1, input().split())
    res = 0
    for i in range(si, ei+1):
        if sj > 0:
            res += dp[i][ej] - dp[i][sj-1]
        else:
            res += dp[i][ej]

    print(res)